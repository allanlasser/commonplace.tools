"use server";

import { z } from "zod";
import { redirect } from "next/navigation";
import { API_URL } from "src/constants";
import { setToken } from "../actions";

const AUTH_PATH = `/api-token-auth/`;

export interface LoginFormState {
  error: string | null;
}

const loginFormSchema = z.object({
  username: z.string(),
  password: z.string(),
  rememberMe: z.string().nullable(),
});

export async function login(
  prevState: LoginFormState,
  formData: FormData
): Promise<LoginFormState> {
  const username = formData.get("username");
  const password = formData.get("password");
  const rememberMe = formData.get("rememberMe");
  const validInput = loginFormSchema.safeParse({
    username,
    password,
    rememberMe,
  });
  try {
    if (!validInput.success) {
      throw new Error(validInput.error.toString());
    }
    const { username, password, rememberMe } = validInput.data;
    const response = await fetch(API_URL + AUTH_PATH, {
      body: JSON.stringify({ username, password }),
      method: "POST",
      headers: { "content-type": "application/json" },
    });
    const { status, statusText } = response;
    const { token, detail } = await response.json();
    if (!response.ok || !token) {
      let message = detail ?? statusText;
      if (status === 400) {
        message = "Invalid username or password. Please try again.";
      }
      throw new Error(message);
    }
    await setToken(token, Boolean(rememberMe));
  } catch (error: Error | unknown) {
    if (error instanceof Error) {
      console.error(error);
      return { error: error.message };
    }
    return { error: `Unexpected error: ${String(error)}` };
  }
  redirect("/");
}
