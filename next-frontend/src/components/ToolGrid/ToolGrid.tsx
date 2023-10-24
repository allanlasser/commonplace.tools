import Link from "next/link";
import Image from "next/image";

import cx from "classnames";

import Text from "src/components/Text";
import Card from "src/components/Card";

import color from "src/styles/color.module.css";
import layout from "src/styles/layout.module.css";
import shape from "src/styles/shape.module.css";
import text from "src/styles/text.module.css";
import styles from "./ToolGrid.module.css";

export interface ToolGridItem {
  id: string;
  name: string;
  owner: string;
  image: string;
}

export default function ToolGrid({ tools }: { tools: ToolGridItem[] }) {
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
          <Link href={`/tools/${tool.id}`} className={styles.link}>
            <Card>
              <Image
                className={cx(styles.image, shape.rounded, color.faded)}
                src={tool.image}
                alt='Placeholder'
                width={600}
                height={600}
              />
              <div className={cx(shape.pv1)}>
                <Text weight='semibold' className={cx(layout.block, color.o70)}>
                  {tool.owner}&rsquo;s
                </Text>
                <Text weight='semibold' size='larger'>
                  <span className={cx(color.faded)}>{tool.name}</span>
                </Text>
              </div>
            </Card>
          </Link>
        </li>
      ))}
      <li>
        <Link href={`/tools/new`} className={cx(styles.link)}>
          <Card className={cx(styles.newTool, color.o70)}>
            <div className={cx(shape.pv1)}>
              <Text weight='bold' size='larger'>
                Add a new tool
              </Text>
            </div>
          </Card>
        </Link>
      </li>
      <li>
        <Link href={`/tools/new`} className={cx(styles.link)}>
          <Card className={cx(styles.requestTool, color.o70)}>
            <div className={cx(shape.pv1)}>
              <Text weight='bold' size='larger'>
                Request a tool
              </Text>
            </div>
          </Card>
        </Link>
      </li>
    </ul>
  );
}
