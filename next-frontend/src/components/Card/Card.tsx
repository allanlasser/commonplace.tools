import cx from "classnames";
import styles from "./Card.module.css";
import font from "src/styles/font.module.css";
import shape from "src/styles/shape.module.css";
import layout from "src/styles/layout.module.css";

export default function Card({
  className,
  children,
}: React.PropsWithChildren<{ className?: string }>) {
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
        font.systemFont,
        className
      )}
    >
      {children}
    </div>
  );
}
