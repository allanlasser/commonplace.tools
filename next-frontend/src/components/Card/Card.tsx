import cx from "classnames";
import styles from "./Card.module.css";
import font from "src/styles/font.module.css";
import shape from "src/styles/shape.module.css";
import layout from "src/styles/layout.module.css";

export default function Card({ children }: React.PropsWithChildren) {
  let pos = Math.random() >= 0.5 ? 1 : -1;
  const rand = Math.random();
  return (
    <div
      className={cx(
        styles.card,
        layout.flex,
        layout.column,
        layout.justifyEnd,
        shape.p1,
        shape.g1,
        shape.rounded,
        font.systemFont
      )}
      style={{ transform: `rotate(${pos * rand}deg)` }}
    >
      {children}
    </div>
  );
}
