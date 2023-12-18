/* Provide a method for a client to fetch the server's session token cookie, if it exists. */
import { redirect } from "next/navigation";
import { getToken, deleteToken } from "src/app/auth/actions";

export async function GET() {
  const token = getToken();
  return Response.json({ token });
}

export async function DELETE() {
  deleteToken();
  redirect("/");
}
