import Image from "next/image";
import { Inter } from "next/font/google";
import styles from "./page.module.css";
import cx from "classnames";
import Link from "next/link";

const inter = Inter({ subsets: ["latin"] });

interface Tool {
  id: string;
  name: string;
  owner: string;
  image: string;
}

const tools = [
  {
    id: "1",
    name: "Hammer",
    owner: "Allan",
    image: "/placeholder.png",
  },
  {
    id: "2",
    name: "Wheelbarrow",
    owner: "Chris",
    image: "/placeholder.png",
  },
];

interface TextOptions {
  size?: "smaller" | "larger";
  weight?: "semibold" | "bold";
}

function Text({
  size,
  weight,
  children,
}: React.PropsWithChildren<TextOptions>) {
  return (
    <p className={cx(size && styles[size], weight && styles[weight])}>
      {children}
    </p>
  );
}

function Card({ children }: React.PropsWithChildren) {
  const rand = (Math.random() * 10) % 5;
  return (
    <div
      className={cx(styles.card, styles.systemFont, styles.rounded)}
      style={{ transform: `rotate(${rand} deg)` }}
    >
      {children}
    </div>
  );
}

function ToolList({ tools }: { tools: Tool[] }) {
  return (
    <ul
      className={cx(
        styles.noListStyle,
        styles.m2,
        styles.grid,
        styles.g1,
        styles.col3
      )}
    >
      {tools.map((tool) => (
        <li key={tool.id}>
          <Card>
            <Image
              className={cx(styles.image, styles.rounded)}
              src={tool.image}
              alt='Placeholder'
              width={600}
              height={600}
            />
            <div className={cx(styles.pv1)}>
              <Text weight='semibold' size='larger'>
                <span className={cx(styles.faded)}>
                  {tool.owner}&rsquo; {tool.name}
                </span>
              </Text>
            </div>
          </Card>
        </li>
      ))}
    </ul>
  );
}

function SiteName() {
  return (
    <Link
      href='/'
      className={cx(styles.inlineBlock, styles.larger, styles.hoverGlow)}
    >
      <h1
        className={cx(
          styles.systemFont,
          styles.upperCase,
          styles.o90,
          styles.p2,
          styles.larger
        )}
      >
        <span
          className={cx(
            styles["c-braun-green"],
            styles.block,
            styles.o90,
            styles.larger
          )}
        >
          common
        </span>
        <span
          className={cx(
            styles["c-braun-yellow"],
            styles.block,
            styles.o90,
            styles.larger
          )}
        >
          place
        </span>
        <span className={cx(styles["c-braun-red"], styles.o70, styles.larger)}>
          .
        </span>
        <span
          className={cx(
            styles["c-braun-orange"],
            styles.lowerCase,
            styles.o70,
            styles.larger
          )}
        >
          tools
        </span>
      </h1>
    </Link>
  );
}

export default function Home() {
  return (
    <main className={cx(styles.page, styles.vh100)}>
      <SiteName />
      <ToolList tools={tools} />
    </main>
  );
}
