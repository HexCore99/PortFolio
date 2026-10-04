<script lang="ts">
	import { asset } from '$app/paths';
	import type { AssetPath } from '$app/types';
	let { name }: { name: string } = $props();
	const icons: Record<string, string> = {
		Rust: 'rust',
		Python: 'python',
		'C++': 'cplusplus',
		JavaScript: 'javascript',
		SvelteKit: 'svelte',
		React: 'react',
		'Next.js': 'nextdotjs',
		Vite: 'vite',
		'Tailwind CSS': 'tailwindcss',
		'Redux Toolkit': 'redux',
		'React Router': 'reactrouter',
		Express: 'express',
		Flask: 'flask',
		MySQL: 'mysql',
		SQLite: 'sqlite',
		JWT: 'jsonwebtokens',
		'TensorFlow/Keras': 'tensorflow',
		'Tauri 2': 'tauri',
		raylib: 'raylib'
	};
</script>

{#if icons[name]}
	<img
		src={asset(`skills/${icons[name]}.svg` as AssetPath)}
		alt=""
		width="19"
		height="19"
		loading="lazy"
	/>
{:else}
	<svg
		width="19"
		height="19"
		viewBox="0 0 24 24"
		fill="none"
		stroke="currentColor"
		stroke-width="1.7"
		stroke-linecap="round"
		stroke-linejoin="round"
		aria-hidden="true"
	>
		{#if name === 'C'}
			<path d="m12 2 9 5v10l-9 5-9-5V7Z" /><path d="M16 8a6 6 0 1 0 0 8" />
		{:else if name === 'TypeScript'}
			<rect x="2" y="2" width="20" height="20" rx="1" fill="currentColor" stroke="none" />
			<path
				d="M5 10h6m-3 0v9m11-8c-4-3-7 1-3 3l1 .5c4 2 1 6-3 3"
				stroke="var(--skill-background, white)"
				stroke-width="1.8"
			/>
		{:else if name === 'SDL3'}
			<rect x="2" y="3" width="20" height="15" rx="2" /><path
				d="M8 22h8m-4-4v4M6 8h5m-5 4h3m6-4 3 3-3 3"
			/>
		{:else if name === 'Java'}
			<path
				d="M5 10h12v6a5 5 0 0 1-5 5H10a5 5 0 0 1-5-5Zm12 1h2a3 3 0 0 1 0 6h-2M9 7c-3-3 3-3 0-6m5 6c-3-3 3-3 0-6"
			/>
		{:else if name === 'Zustand'}
			<circle cx="6" cy="6" r="3" /><circle cx="18" cy="6" r="3" /><rect
				x="4"
				y="5"
				width="16"
				height="16"
				rx="7"
				fill="var(--white)"
			/><path d="M8 11h.01M16 11h.01m-6 4h4l-2 2Z" />
		{:else if name === 'CLI tools'}
			<rect x="2" y="3" width="20" height="18" rx="3" /><path d="m6 8 4 4-4 4m7 0h5" />
		{:else}
			<path d="M3 5h7l2 3h9v12H3Z" /><path d="M7 13h3v3H7Zm7 0h3v3h-3Z" />
		{/if}
	</svg>
{/if}

<style>
	img,
	svg {
		flex: 0 0 19px;
		display: block;
		object-fit: contain;
	}
</style>
