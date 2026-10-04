<script lang="ts">
	import { onMount } from 'svelte';
	type Theme = 'light' | 'dark';
	let theme = $state<Theme>('light');

	onMount(() => {
		theme = document.documentElement.dataset.theme === 'dark' ? 'dark' : 'light';
		updateThemeColor();
	});

	function updateThemeColor() {
		document
			.querySelector('meta[name="theme-color"]')
			?.setAttribute('content', theme === 'dark' ? '#101826' : '#f6f3ea');
	}

	function toggleTheme() {
		theme = theme === 'light' ? 'dark' : 'light';
		document.documentElement.dataset.theme = theme;
		document.documentElement.style.colorScheme = theme;
		updateThemeColor();
		try {
			localStorage.setItem('demo-folio-theme', theme);
		} catch {
			// The theme still applies when browser storage is unavailable.
		}
	}
</script>

<button
	type="button"
	class="theme-toggle"
	aria-label={theme === 'light' ? 'Switch to dark theme' : 'Switch to light theme'}
	title={theme === 'light' ? 'Switch to dark theme' : 'Switch to light theme'}
	onclick={toggleTheme}
>
	{#if theme === 'light'}
		<svg viewBox="0 0 24 24" aria-hidden="true">
			<path d="M20.4 15.2A8.6 8.6 0 0 1 8.8 3.6 8.7 8.7 0 1 0 20.4 15.2Z" />
		</svg>
	{:else}
		<svg viewBox="0 0 24 24" aria-hidden="true">
			<circle cx="12" cy="12" r="4" /><path
				d="M12 2v2m0 16v2M4.9 4.9l1.4 1.4m11.4 11.4 1.4 1.4M2 12h2m16 0h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"
			/>
		</svg>
	{/if}
	<span>{theme === 'light' ? 'Dark' : 'Light'}</span>
</button>

<style>
	.theme-toggle {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		gap: 8px;
		min-height: 44px;
		padding: 9px 12px;
		border: 1.5px solid var(--ink);
		border-radius: 5px;
		background: var(--surface-control);
		color: var(--ink);
		box-shadow: 0 3px 0 var(--control-shadow);
		font: 700 11px var(--mono);
		transition:
			background 0.2s,
			transform 0.2s,
			box-shadow 0.2s;
	}
	.theme-toggle:hover {
		background: var(--blue-soft);
		transform: translateY(-2px);
		box-shadow: 0 5px 0 var(--control-shadow);
	}
	.theme-toggle:active {
		transform: translateY(1px);
		box-shadow: 0 1px 0 var(--control-shadow);
	}
	svg {
		width: 18px;
		height: 18px;
		fill: none;
		stroke: currentColor;
		stroke-width: 1.8;
		stroke-linecap: round;
		stroke-linejoin: round;
	}
	@media (max-width: 700px) {
		.theme-toggle {
			width: 100%;
			justify-content: space-between;
			padding: 12px;
		}
	}
	@media (prefers-reduced-motion: reduce) {
		.theme-toggle:hover,
		.theme-toggle:active {
			transform: none;
		}
	}
</style>
