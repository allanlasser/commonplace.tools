"use client";

import { useFormState, useFormStatus } from "react-dom";
import { login, LoginFormState } from "./action";

function Submit({ children }: React.PropsWithChildren) {
  const { pending } = useFormStatus();
  return (
    <button type='submit' aria-disabled={pending}>
      {children}
    </button>
  );
}

export default function LoginPage() {
  const [state, formAction] = useFormState<LoginFormState, FormData>(login, {
    error: null,
  });

  return (
    <div>
      <form action={formAction}>
        <label>
          Username
          <input type='text' name='username' required />
        </label>
        <label>
          Password
          <input type='password' name='password' required />
        </label>
        <label>
          Remember Me <input type='checkbox' name='rememberMe' />
        </label>
        <Submit>Log In</Submit>
      </form>
      {state?.error && <p style={{ color: "red" }}>{state.error}</p>}
    </div>
  );
}
