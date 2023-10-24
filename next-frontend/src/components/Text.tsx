import cx from "classnames";
import fontStyles from "src/styles/font.module.css";
import textStyles from "src/styles/text.module.css";

interface TextOptions {
  family?: "Inter" | "System";
  size?: "smaller" | "larger";
  weight?: "semibold" | "bold";
  transform?: "lowerCase" | "upperCase";
  className?: string;
}

export default function Text({
  family,
  size,
  weight,
  transform,
  className,
  children,
}: React.PropsWithChildren<TextOptions>) {
  return (
    <span
      className={cx(
        family && fontStyles[family],
        size && fontStyles[size],
        weight && fontStyles[weight],
        transform && textStyles[transform],
        className
      )}
    >
      {children}
    </span>
  );
}
