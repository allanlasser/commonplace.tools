import { getToolList } from '@/data/tools';
import { getUser } from '@/data/users';

interface Params {
	id: string;
}

export async function load({ params }: { params: Params }) {
	const { id } = params;
	const user = getUser(id);
	const tools = await getToolList({ owner: id });
	console.log(tools);
	return {
		user,
		tools
	};
}
