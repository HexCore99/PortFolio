<script lang="ts">
	let {
		name,
		size = 20
	}: { name: 'arrow' | 'down' | 'github' | 'linkedin' | 'mail' | 'code'; size?: number } = $props();
</script>

<svg
	width={size}
	height={size}
	viewBox="0 0 24 24"
	fill="none"
	stroke="currentColor"
	stroke-width="1.6"
	stroke-linecap="round"
	stroke-linejoin="round"
	aria-hidden="true"
>
	{#if name === 'arrow'}
		<path d="M7 17 17 7M7 7h10v10" />
	{:else if name === 'down'}
		<path d="M12 4v16m-6-6 6 6 6-6" />
	{:else if name === 'mail'}
		<rect x="3" y="5" width="18" height="14" rx="2" /><path d="m3 6 9 7 9-7" />
	{:else if name === 'code'}
		<path d="m8 6-6 6 6 6m8-12 6 6-6 6m-3-15-2 18" />
	{:else if name === 'linkedin'}
		<path d="M5 9v11M5 4v.1M10 20V9h4v2c1-3 6-3 6 2v7M14 12v8" /><circle cx="5" cy="4" r="1" />
	{:else if name === 'github'}
		<path
			d="M9 19c-4 1-4-2-6-2m12 5v-4c0-1 .1-1.8-.5-2.4 3.3-.4 6.5-1.6 6.5-7A5.4 5.4 0 0 0 19.5 5c.2-.8.2-2-.2-3 0 0-1.3-.4-4.3 1.6a14 14 0 0 0-6 0C6 1.6 4.7 2 4.7 2c-.4 1-.4 2.2-.2 3A5.4 5.4 0 0 0 3 8.6c0 5.4 3.2 6.6 6.5 7C9 16.2 9 17 9 18v4"
		/>
	{/if}
</svg>
