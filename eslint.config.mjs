import { dirname } from "path";
import { fileURLToPath } from "url";
import { FlatCompat } from "@eslint/eslintrc";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const compat = new FlatCompat({
  baseDirectory: __dirname,
});

const eslintConfig = [
  ...compat.extends("next/core-web-vitals", "plugin:@typescript-eslint/recommended", "prettier"),
  {
    plugins: ["@typescript-eslint"],
    rules: {
      "@typescript-eslint/no-unused-vars": ["error"],
      "react/react-in-jsx-scope": "off"
    }
  }
];

export default eslintConfig;
