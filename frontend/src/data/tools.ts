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

export async function getToolList() {
	return getList<LendablesResult>('lendables');
}

export async function getTool(id: string) {
	return getSingle<LendablesResult>(`lendables/${id}`);
}
