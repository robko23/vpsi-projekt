import "dotenv/config"
import { migrate } from "drizzle-orm/libsql/migrator"
import { db, connection } from "./src/schema"
 
// This will run migrations on the database, skipping the ones already applied
await migrate(db, { migrationsFolder: "./drizzle" })
 
// Don't forget to close the connection, otherwise the script will hang
connection.close()
