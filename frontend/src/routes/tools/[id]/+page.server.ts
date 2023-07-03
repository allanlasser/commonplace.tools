import { getResource } from '@/data/api';
import { getTool } from '@/data/tools';
import type { LocationResult } from '@/data/location';
import type { LendableStatusResult } from '@/data/status';
import type { UserResult } from '@/data/users';
import { getLoanList, type LoanResult } from '@/data/loan.js';

interface UnwrappedLoanResult extends LoanResult {
	borrowing_user_data?: UserResult;
}

export async function load({ params }: { params: { id: string } }) {
	const tool = await getTool(params.id);
	const owner = await getResource<UserResult>(tool.owner);
	const location = tool.location ? await getResource<LocationResult>(tool.location) : null;
	const status = await getResource<LendableStatusResult>(tool.lendable_status);
	const history = await getLoanList({ lendable: params.id });
	const historyWithUsers = await Promise.all(
		history.results.map<Promise<UnwrappedLoanResult>>(async (result) => {
			const user = await getResource<UserResult>(result.borrowing_user);
			return {
				...result,
				borrowing_user_data: user
			};
		})
	);
	return {
		tool,
		owner,
		location,
		status,
		history: { ...history, results: historyWithUsers }
	};
}
