export const runtime = "nodejs"; // 👈 Force Next.js to use Node.js runtime

import { handlers } from "@/auth" // Referring to the auth.ts we just created
export const { GET, POST } = handlers
