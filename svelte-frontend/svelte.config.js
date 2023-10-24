import adapter from '@sveltejs/adapter-node';
import { vitePreprocess } from '@sveltejs/kit/vite';
import path from "path"

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://kit.svelte.dev/docs/integrations#preprocessors
	// for more information about preprocessors
	preprocess: vitePreprocess(),

	kit: {
    // we use the `adapter-node` to run our own Node server
		adapter: adapter(),
    alias: {
      // this will match a directory and its contents
      '@': path.resolve('./src'),
    },
	}
};

export default config;
