import { credentials, db, users } from "@/schema";
import { eq } from "drizzle-orm";

export async function getUserFromDb(email: string) {
	const user = await db.select().from(users).where(eq(users.email, email)).limit(1);
	if (!user.length) return null;

	const cred = await db
		.select({ passwordHash: credentials.passwordHash })
		.from(credentials)
		.where(eq(credentials.userId, user[0].id))
		.limit(1);

	return cred.length ? { ...user[0], passwordHash: cred[0].passwordHash } : null;
}
