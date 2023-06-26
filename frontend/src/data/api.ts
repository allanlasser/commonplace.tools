import qs from 'query-string';
import { API_URL } from '@/constants';

async function get<R>(resource: string, params?: Record<string, unknown>): Promise<R> {
	const query = qs.stringify({ ...params, format: 'json' });
	const url = [API_URL, resource].join('/') + '?' + query;
	const res = await fetch(url);
	const json = await res.json();
	return json;
}

/** Gets a single result from the API in JSON format */
export async function getSingle<R>(resource: string, params?: Record<string, unknown>): Promise<R> {
	return get<R>(resource, params);
}

export interface PaginatedResponse<R> {
	count: number;
	next: string | null;
	previous: string | null;
	results: R[];
}

export async function getList<R>(
	resource: string,
	params?: Record<string, unknown>
): Promise<PaginatedResponse<R>> {
	return get<PaginatedResponse<R>>(resource, params);
}

export async function getResource<R>(url: string): Promise<R> {
	const res = await fetch(url);
	const json = await res.json();
	return json;
}
