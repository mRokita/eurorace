import adapter from '@sveltejs/adapter-auto';
import sveltePreprocess from 'svelte-preprocess';
import { preprocess } from 'svelte/compiler';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter()
	},
	preprocess: preprocess()
};

export default config;