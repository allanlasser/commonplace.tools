import { getToolList } from '@/data/tools';

export async function load() {
  const tools = await getToolList();
  return {
    tools
  };
}