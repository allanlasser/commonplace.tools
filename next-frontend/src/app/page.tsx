import Image from "next/image";
import styles from "./page.module.css";
import cx from "classnames";

import { type Tool, tools } from "src/data/tools";
import Text from "src/components/Text";
import Card from "src/components/Card";

import color from "src/styles/color.module.css";
import layout from "src/styles/layout.module.css";
import shape from "src/styles/shape.module.css";
import text from "src/styles/text.module.css";
import SiteName from "src/components/SiteName";

function ToolList({ tools }: { tools: Tool[] }) {
  return (
    <ul
      className={cx(
        text.noListStyle,
        shape.m2,
        shape.g1,
        layout.grid,
        layout.col3
      )}
    >
      {tools.map((tool) => (
        <li key={tool.id}>
          <Card>
            <Image
              className={cx(styles.image, shape.rounded, color.faded)}
              src={tool.image}
              alt='Placeholder'
              width={600}
              height={600}
            />
            <div className={cx(shape.pv1)}>
              <Text weight='semibold' size='larger'>
                <span className={cx(color.faded)}>
                  {tool.owner}&rsquo;s {tool.name}
                </span>
              </Text>
            </div>
          </Card>
        </li>
      ))}
    </ul>
  );
}

export default function Home() {
  return (
    <main className={cx(styles.page, shape.vh100)}>
      <SiteName />
      <h2 className={cx(shape.p2, color.faded)}>
        <span className={cx(text.upperCase, color.faded)}>Windsor Park</span>
      </h2>
      <ToolList tools={tools} />
    </main>
  );
}
