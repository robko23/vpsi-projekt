import NextAuth from "next-auth"
import Credentials from "next-auth/providers/credentials"
import { DrizzleAdapter } from "@auth/drizzle-adapter"
import { signInSchema } from "./lib/zod"
import { accounts, db, sessions, users, verificationTokens } from "./schema"

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
				let user = null

				const { email, password } = await signInSchema.parseAsync(credentials)

				// logic to salt and hash password
				const pwHash = saltAndHashPassword(password)

				// logic to verify if the user exists
				user = await getUserFromDb(email, pwHash)

				if (!user) {
					// No user found, so this is their first attempt to login
					// Optionally, this is also the place you could do a user registration
					throw new Error("Invalid credentials.")
				}

				// return user object with their profile data
				return user
			},
		})
	],
})
