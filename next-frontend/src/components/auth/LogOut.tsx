"use client";

import { useRouter } from "next/navigation";

export default function LogOut() {
  const router = useRouter();
  async function handleLogOut() {
    await fetch("/api/token", { method: "DELETE" });
    router.refresh();
  }
  return <button onClick={handleLogOut}>Log Out</button>;
}
