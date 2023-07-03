import { getLoanList } from '@/data/loan';
import { getToolList } from '@/data/tools';
import { getUser } from '@/data/users';

interface Params {
	id: string;
}

export async function load({ params }: { params: Params }) {
	const { id } = params;
	const user = getUser(id);
	const tools = getToolList({ owner: id });
	const loans = getLoanList({
		borrowing_user: id,
		return_confirmed_by_borrower: false,
		return_confirmed_by_lender: false
	});
	return {
		user,
		tools,
		loans
	};
}
