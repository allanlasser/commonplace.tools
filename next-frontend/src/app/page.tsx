import styles from "./page.module.css";
import cx from "classnames";

import { tools } from "src/data/tools";

import shape from "src/styles/shape.module.css";
import ToolGrid from "src/components/ToolGrid";
import Link from "next/link";
import { getToken } from "./auth/actions";

export default async function Home() {
  const token = await getToken();
  return (
    <main className={cx(styles.page, shape.vh100)}>
      {token ? (
        <ToolGrid tools={tools} />
      ) : (
        <p>
          <Link href='/auth/login'>Log in to view tools</Link>
        </p>
      )}
    </main>
  );
}
