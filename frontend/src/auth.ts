import NextAuth from "next-auth"
import Credentials from "next-auth/providers/credentials"
import { DrizzleAdapter } from "@auth/drizzle-adapter"
import { signInSchema } from "./lib/zod"
import { accounts, db, sessions, users, verificationTokens } from "./schema"
import { hash, verify } from 'argon2'
import { getUserFromDb } from "./db_query/user"

export const { handlers, signIn, signOut, auth } = NextAuth({
	adapter: DrizzleAdapter(db, {
		usersTable: users,
		accountsTable: accounts,
		sessionsTable: sessions,
		verificationTokensTable: verificationTokens,
	}),
	providers: [
		Credentials({
			// You can specify which fields should be submitted, by adding keys to the `credentials` object.
			// e.g. domain, username, password, 2FA token, etc.
			credentials: {
				email: {},
				password: {},
			},
			authorize: async (credentials) => {
				const { email, password } = await signInSchema.parseAsync(credentials)

				const user = await getUserFromDb(email)
				if (!user) {
					throw new Error("Invalid username or password")
				}

				const success = await verify(user.passwordHash, password)
				if (!success) {
					throw new Error("Invalid username or password")
				}

				return user
			},
		})
	],
})
