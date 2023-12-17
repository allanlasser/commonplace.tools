import SiteName from "src/components/SiteName";
import Link from "next/link";
import { getToken } from "src/app/auth/actions";
import LogOut from "../auth/LogOut";

export default async function Navigation() {
  const token = await getToken();
  return (
    <nav>
      <SiteName />
      {!token ? <Link href='/auth/login'>Log In</Link> : <LogOut />}
    </nav>
  );
}
