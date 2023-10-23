export interface GetResponse {
  name: string;
}

export async function GET() {
  return Response.json({ name: "John Doe" });
}
