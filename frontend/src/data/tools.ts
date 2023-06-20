import { API_URL } from "@/constants";
import { getList, getSingle } from "./api";

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
  return getList<LendablesResult>(API_URL + '/lendables/?format=json');
}

export async function getTool(id: string) {
  return getSingle<LendablesResult>(API_URL + `/lendables/${id}?format=json`);
}
