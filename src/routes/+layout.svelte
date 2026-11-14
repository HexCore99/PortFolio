<script lang="ts">
	import './layout.css';
	import { asset } from '$app/paths';
	import { dev } from '$app/env';
	import { onMount } from 'svelte';
	import { inject } from '@vercel/analytics';

	let { children } = $props();
	const faviconHref = `${asset('favicon.svg')}?v=2`;

	onMount(() => {
		inject({ mode: dev ? 'development' : 'production' });
	});
</script>

<svelte:head>
	<link rel="icon" type="image/svg+xml" href={faviconHref} />
</svelte:head>
{@render children()}
