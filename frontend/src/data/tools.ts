import { getList, getSingle } from './api';

export interface LendablesResult {
	id: number;
	url: string;
	name: string;
	owner: string;
	created: string;
	modified: string;
	replacement_cost: string;
	lendable_status: string;
	lendable_type: string;
	location: string | null;
	location_updated: string | null;
}

export interface ToolFilters {
	owner?: string;
}

export async function getToolList(filters?: ToolFilters, ordering?: string) {
	return getList<LendablesResult>('lendables', { ...filters, ordering });
}

export async function getTool(id: string) {
	return getSingle<LendablesResult>(`lendables/${id}`);
}
