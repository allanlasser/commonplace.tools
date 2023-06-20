import { getSingle } from '@/data/api';
import { getTool } from '@/data/tools';
import type { LocationResult } from '@/data/location';
import type { LendableStatusResult } from '@/data/status';
import type { UserResult } from '@/data/users';

export async function load({ params }) {
  const tool = await getTool(params.id);
  const owner = await getSingle<UserResult>(tool.owner);
  const location = tool.location ? await getSingle<LocationResult>(tool.location) : null;
  const status = await getSingle<LendableStatusResult>(tool.lendable_status);
  return {
    tool,
    owner,
    location,
    status
  }
}