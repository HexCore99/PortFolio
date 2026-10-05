<script lang="ts">
	import './layout.css';
	import { asset } from '$app/paths';
	let { children } = $props();
	const faviconHref = `${asset('favicon.svg')}?v=2`;
</script>

<svelte:head>
	<link rel="icon" type="image/svg+xml" href={faviconHref} />
</svelte:head>
{@render children()}
