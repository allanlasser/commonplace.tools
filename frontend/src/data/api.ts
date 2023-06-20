/** Gets a single result from the API in JSON format */
export async function getSingle<R>(url: string): Promise<R> {
  const res = await fetch(url);
  const json = await res.json();
  return json;
}

export interface PaginatedResponse<R> {
  count: number;
  next: string | null;
  previous: string | null;
  results: R[];
}

export async function getList<R>(url: string): Promise<PaginatedResponse<R>> {
  const res = await fetch(url);
  const json = await res.json();
  return json;
}