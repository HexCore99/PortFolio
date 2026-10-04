<script lang="ts">
	import { NeoButton } from '@dvcol/neo-svelte/buttons';
	import Icon from './Icon.svelte';
	import { profile } from '#lib/data/portfolio.js';
	let open = $state(false);
	let menuButton = $state<HTMLButtonElement>();
	const links = [
		{ href: '#top', label: 'Home' },
		{ href: '#work', label: 'Work' },
		{ href: '#about', label: 'About' },
		{ href: '#contact', label: 'Contact' }
	];
	function closeMenu(event: KeyboardEvent) {
		if (event.key === 'Escape' && open) {
			open = false;
			menuButton?.focus();
		}
	}
</script>

<svelte:window onkeydown={closeMenu} />
<header class="site-header">
	<div class="nav-inner container">
		<a
			class="brand"
			href="#top"
			aria-label="Siabul Hassan, back to top"
			onclick={() => (open = false)}
			><span class="brand-symbol">sh.</span><span class="brand-name">Siabul Hassan</span></a
		>
		<NeoButton
			elevation={0}
			hover={0}
			active={0}
			scale={false}
			bind:ref={menuButton}
			class="menu-toggle"
			aria-expanded={open}
			aria-controls="main-navigation"
			aria-label={open ? 'Close navigation menu' : 'Open navigation menu'}
			onclick={() => (open = !open)}
		>
			<span>{open ? 'Close' : 'Menu'}</span><span class="menu-lines" class:expanded={open}
				><i></i><i></i></span
			>
		</NeoButton>
		<nav class:open aria-label="Main navigation" id="main-navigation">
			{#each links as link (link.href)}<a
					class="nav-tab"
					href={link.href}
					onclick={() => (open = false)}>{link.label}</a
				>{/each}
			<NeoButton
				class="nav-mail"
				elevation={0}
				hover={0}
				active={0}
				scale={false}
				href={'mailto:' + profile.email}
				aria-label="Email Siabul Hassan"
				><span>Email me</span><Icon name="arrow" size={17} /></NeoButton
			>
		</nav>
	</div>
</header>

<style>
	.site-header {
		position: sticky;
		top: 0;
		z-index: 20;
		background: var(--paper);
		border-bottom: 1px solid var(--line);
	}
	.nav-inner {
		min-height: 86px;
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 24px;
	}
	.brand {
		display: inline-flex;
		align-items: center;
		gap: 12px;
		text-decoration: none;
	}
	.brand-symbol {
		display: grid;
		place-items: center;
		height: 42px;
		width: 42px;
		border: 1.5px solid var(--ink);
		background: #e9b58d;
		color: var(--ink);
		border-radius: 12px 4px 12px 4px;
		box-shadow: 2px 2px 0 var(--ink);
		font-weight: 850;
		letter-spacing: -1.5px;
		font-size: 24px;
		padding-bottom: 4px;
	}
	.brand-name {
		font-size: 14px;
		font-weight: 750;
		letter-spacing: -0.3px;
	}
	nav {
		display: flex;
		align-items: center;
		gap: 10px;
	}
	nav a {
		font-size: 13px;
		font-weight: 600;
		text-decoration: none;
		padding-block: 10px;
		min-height: 40px;
		display: inline-flex;
		align-items: center;
	}
	nav a:hover {
		color: var(--blue);
	}
	nav a:first-child {
		display: none;
	}
	nav :global(.nav-mail) {
		display: inline-flex;
		gap: 20px;
		align-items: center;
		border: 1.5px solid var(--ink);
		border-radius: 5px;
		padding: 10px 15px;
		background: var(--ink);
		color: white;
		box-shadow: 0 3px 0 #8b9cb2;
	}
	nav :global(.nav-mail):hover {
		background: #294565;
	}
	:global(.menu-toggle) {
		display: none;
	}
	@media (max-width: 700px) {
		.nav-inner {
			min-height: 74px;
		}
		.brand-symbol {
			width: 36px;
			height: 36px;
			font-size: 21px;
		}
		.brand-name {
			font-size: 12px;
		}
		:global(.menu-toggle) {
			display: inline-flex;
			align-items: center;
			gap: 10px;
			min-height: 44px;
			border: 1.5px solid var(--ink);
			border-radius: 5px;
			padding: 9px 12px;
			background: var(--white);
			box-shadow: 0 3px 0 var(--ink);
			font-size: 11px;
			font-weight: 700;
		}
		.menu-lines {
			display: grid;
			gap: 5px;
			width: 15px;
		}
		.menu-lines i {
			height: 1.5px;
			background: currentColor;
			transition: transform 0.2s;
		}
		.expanded i:first-child {
			transform: translateY(3.25px) rotate(45deg);
		}
		.expanded i:last-child {
			transform: translateY(-3.25px) rotate(-45deg);
		}
		nav {
			display: none;
			position: absolute;
			top: 100%;
			left: 0;
			right: 0;
			background: var(--paper);
			padding: 12px 22px 24px;
			border-bottom: 1.5px solid var(--ink);
			box-shadow: 0 7px 0 #182a4110;
		}
		nav.open {
			display: flex;
			flex-direction: column;
			align-items: stretch;
			gap: 2px;
		}
		nav a,
		nav a:first-child {
			display: flex;
			padding: 13px 4px;
			min-height: 46px;
		}
		nav :global(.nav-mail) {
			justify-content: space-between;
			padding: 12px;
			margin-top: 8px;
		}
	}

	nav .nav-tab {
		min-height: 44px;
		padding: 10px 17px;
		border: 1.5px solid #31465e;
		border-radius: 5px;
		background: #dce5ee;
		color: #243a53;
		box-shadow: 0 3px 0 #8b9cb2;
		transition:
			background 0.2s,
			box-shadow 0.2s,
			translate 0.2s;
	}
	nav .nav-tab:hover,
	nav .nav-tab:focus-visible {
		background: #dce6f6;
		translate: 0 -2px;
		box-shadow: 0 5px 0 #8b9cb2;
	}
	nav .nav-tab:active {
		translate: 0 1px;
		box-shadow: 0 1px 0 #8b9cb2;
	}
	@media (max-width: 700px) {
		nav.open {
			gap: 10px;
		}
		nav .nav-tab,
		nav .nav-tab:first-child {
			padding: 12px 16px;
		}
	}
	@media (prefers-reduced-motion: reduce) {
		nav .nav-tab:hover,
		nav .nav-tab:active {
			translate: none;
		}
	}
</style>
