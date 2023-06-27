import { getSingle } from './api';

export interface UserResult {
	id: number;
	url: number;
	username: string;
	first_name: string;
	last_name: string;
	email: string;
	is_staff: boolean;
	is_active: boolean;
	last_login: string;
	date_joined: string;
}

export async function getUser(id: number): Promise<UserResult> {
	return getSingle<UserResult>(`users/${id}`);
}
