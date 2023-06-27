import { getList, getSingle } from './api';

export interface LoanResult {
	id: number;
	url: string;
	start_date: string;
	end_date: string;
	created: string;
	modified: string;
	confirmed_by_lender: string;
	confirmed_by_borrower: string;
	returned_datetime: string;
	return_confirmed_by_borrower: string;
	return_confirmed_by_lender: string;
	lendable: string;
	borrowing_user: string;
}

export interface LoanFilters {
	lendable?: string | number;
	lendable__owner?: string | number;
	borrowing_user?: string | number;
}

export async function getLoanList(filters?: LoanFilters, ordering?: string) {
	return getList<LoanResult>('loans', { ...filters, ordering });
}

export async function getLoan(id: string) {
	return getSingle<LoanResult>(`loans/${id}`);
}
