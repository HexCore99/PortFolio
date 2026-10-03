<script lang="ts">
	import Icon from './Icon.svelte';
	import { profile } from '#lib/data/portfolio.js';
	let open = $state(false);
	let menuButton: HTMLButtonElement;
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
			onclick={() => (open = false)}>SIABUL<span>_</span></a
		>
		<button
			bind:this={menuButton}
			class="menu-toggle"
			aria-expanded={open}
			aria-controls="main-navigation"
			aria-label={open ? 'Close navigation menu' : 'Open navigation menu'}
			onclick={() => (open = !open)}
		>
			<span>{open ? 'Close' : 'Menu'}</span><span class="menu-lines" class:expanded={open}
				><i></i><i></i></span
			>
		</button>
		<nav class:open aria-label="Main navigation" id="main-navigation">
			{#each links as link (link.href)}<a href={link.href} onclick={() => (open = false)}
					>{link.label}</a
				>{/each}
			<a class="nav-mail" href={'mailto:' + profile.email} aria-label="Email Siabul Hassan"
				><Icon name="mail" size={17} /></a
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
		border-bottom: 2px solid var(--ink);
	}
	.nav-inner {
		min-height: 72px;
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 24px;
	}
	.brand {
		font-size: 20px;
		font-weight: 950;
		letter-spacing: -0.8px;
		text-decoration: none;
	}
	.brand span {
		color: #a33632;
	}
	nav {
		display: flex;
		align-items: center;
		gap: 9px;
	}
	nav a,
	.menu-toggle {
		border: 2px solid var(--ink);
		border-radius: 3px;
		background: var(--stone);
		color: white;
		box-shadow: 3px 3px 0 var(--ink);
		padding: 10px 12px;
		font: 700 10px var(--mono);
		text-transform: uppercase;
		text-decoration: none;
		min-height: 37px;
		transition:
			transform 0.15s,
			box-shadow 0.15s;
	}
	nav a:first-child {
		background: var(--olive);
		color: var(--ink);
	}
	nav a:nth-child(4) {
		background: var(--mauve);
		color: var(--ink);
	}
	nav a:hover {
		transform: translate(2px, 2px);
		box-shadow: 1px 1px 0 var(--ink);
	}
	nav .nav-mail {
		padding: 8px 10px;
	}
	.menu-toggle {
		display: none;
	}
	@media (max-width: 700px) {
		.nav-inner {
			min-height: 66px;
		}
		.menu-toggle {
			display: inline-flex;
			align-items: center;
			gap: 12px;
			min-height: 40px;
		}
		.menu-lines {
			display: grid;
			gap: 5px;
			width: 16px;
		}
		.menu-lines i {
			height: 2px;
			background: currentColor;
			transition: transform 0.2s;
		}
		.expanded i:first-child {
			transform: translateY(3.5px) rotate(45deg);
		}
		.expanded i:last-child {
			transform: translateY(-3.5px) rotate(-45deg);
		}
		nav {
			display: none;
			position: absolute;
			top: 100%;
			left: 0;
			right: 0;
			background: var(--paper);
			padding: 18px 24px 24px;
			border-bottom: 2px solid var(--ink);
		}
		nav.open {
			display: flex;
			flex-direction: column;
			align-items: stretch;
			gap: 12px;
		}
		nav a {
			padding: 14px;
			min-height: 44px;
		}
		nav .nav-mail {
			padding: 12px;
		}
	}
</style>
