import styles from "./page.module.css";
import cx from "classnames";

import { tools } from "src/data/tools";

import color from "src/styles/color.module.css";
import shape from "src/styles/shape.module.css";
import text from "src/styles/text.module.css";
import SiteName from "src/components/SiteName";
import ToolGrid from "src/components/ToolGrid";

export default function Home() {
  return (
    <main className={cx(styles.page, shape.vh100)}>
      <SiteName />
      <ToolGrid tools={tools} />
    </main>
  );
}
