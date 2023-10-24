import Link from "next/link";
import cx from "classnames";

import Text from "src/components/Text";

import layout from "src/styles/layout.module.css";
import font from "src/styles/font.module.css";
import text from "src/styles/text.module.css";
import color from "src/styles/color.module.css";
import shape from "src/styles/shape.module.css";

export default function SiteName() {
  return (
    <Link
      href='/'
      className={cx(
        shape.m1,
        shape.p1,
        shape.rounded,
        layout.inlineBlock,
        font.larger,
        color.hoverGlow
      )}
    >
      <h1 className={cx(font.Inter, color.o90)}>
        <Text transform='upperCase' className={cx(font.lh1125)}>
          <span className={cx(color["c-braun-green"], color.o90, layout.block)}>
            common
          </span>
          <span
            className={cx(color["c-braun-yellow"], color.o90, layout.block)}
          >
            place
          </span>
          <span className={cx(color["c-braun-red"], text.lowerCase, color.o70)}>
            .
          </span>
          <span
            className={cx(color["c-braun-orange"], text.lowerCase, color.o70)}
          >
            tools
          </span>
        </Text>
      </h1>
    </Link>
  );
}
