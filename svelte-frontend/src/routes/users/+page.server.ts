import { getUserList } from '@/data/users';

export async function load() {
	const users = getUserList();
	return {
		users
	};
}
