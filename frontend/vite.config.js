import tailwindcss from '@tailwindcss/vite';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import path from 'path'; // Add this line


export default defineConfig({
	plugins: [sveltekit(), tailwindcss()],
	resolve: {
		alias: {
			$lib: path.resolve('./src/lib'),
			$assets: path.resolve('./src/assets') // Add this line
		}
	},
	server: {
		proxy: {
			'/api': {
				target: 'http://localhost:8000', // Replace with your backend URL and port
				changeOrigin: true,
				secure: false
			}
		}
	}
})