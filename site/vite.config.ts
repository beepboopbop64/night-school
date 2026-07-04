import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		fs: {
			// Session pages glob-import artifacts from ../sessions/<id>/page/.
			allow: ['..']
		}
	}
});
