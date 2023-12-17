"use server";

import { cookies } from "next/headers";

const AUTH_COOKIE = "auth_token";

const TWO_WEEKS_MS = 12096e5;

export async function setToken(token: string, rememberMe?: boolean) {
  const expires = rememberMe ? new Date(Date.now() + TWO_WEEKS_MS) : undefined;
  cookies().set(AUTH_COOKIE, token, { httpOnly: true, expires });
}

export async function getToken() {
  return cookies().get(AUTH_COOKIE)?.value;
}

export async function deleteToken() {
  cookies().delete(AUTH_COOKIE);
}
