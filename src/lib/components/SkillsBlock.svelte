<script lang="ts">
	import { onMount } from 'svelte';
	import { skills } from '#lib/data/portfolio.js';
	import SkillIcon from './SkillIcon.svelte';

	type Theme = { pastel: string; accent: string; label: string };
	type ChipTheme = { background: string; text: string };

	const groupThemes: Record<string, Theme> = {
		Languages: { pastel: '#f2cdb0', accent: '#f0a979', label: '#7a4a22' },
		Frontend: { pastel: '#c8dfc9', accent: '#7fd1a0', label: '#2d6a4a' },
		'Backend and data': { pastel: '#c9daf0', accent: '#7fb2f0', label: '#2d5384' },
		'Machine learning': { pastel: '#dccbea', accent: '#c29bf0', label: '#6b3f8f' },
		'Desktop and tools': { pastel: '#f1dfa4', accent: '#f0cf6b', label: '#6b5416' }
	};

	const chipThemes: Record<string, ChipTheme> = {
		C: { background: '#6a7bd6', text: '#ffffff' },
		Rust: { background: '#f26b3a', text: '#14213d' },
		Python: { background: '#4b8bbe', text: '#ffffff' },
		'C++': { background: '#00599c', text: '#ffffff' },
		Java: { background: '#f89820', text: '#14213d' },
		JavaScript: { background: '#f7df1e', text: '#14213d' },
		TypeScript: { background: '#3178c6', text: '#ffffff' },
		SvelteKit: { background: '#ff3e00', text: '#14213d' },
		React: { background: '#61dafb', text: '#14213d' },
		'Next.js': { background: '#e8e8e8', text: '#14213d' },
		Vite: { background: '#a78bfa', text: '#14213d' },
		'Tailwind CSS': { background: '#38bdf8', text: '#14213d' },
		'Redux Toolkit': { background: '#764abc', text: '#ffffff' },
		Zustand: { background: '#f0a53a', text: '#14213d' },
		'React Router': { background: '#ef4444', text: '#ffffff' },
		Express: { background: '#b8bec9', text: '#14213d' },
		Flask: { background: '#34d399', text: '#14213d' },
		MySQL: { background: '#4479a1', text: '#ffffff' },
		SQLite: { background: '#4aa3d8', text: '#14213d' },
		JWT: { background: '#fb015b', text: '#ffffff' },
		'TensorFlow/Keras': { background: '#ff8f00', text: '#14213d' },
		'Tauri 2': { background: '#ffc131', text: '#14213d' },
		raylib: { background: '#f2f2f2', text: '#14213d' },
		SDL3: { background: '#3a8fd6', text: '#ffffff' },
		'CLI tools': { background: '#9be564', text: '#14213d' },
		'Windows file-system tooling': { background: '#00a4ef', text: '#14213d' }
	};

	let skillsTree: HTMLDivElement;

	onMount(() => {
		const rows = skillsTree.querySelectorAll<HTMLElement>('.skill-row');
		if (!('IntersectionObserver' in window)) {
			rows.forEach((row) => row.classList.add('is-visible'));
			return;
		}

		const observer = new IntersectionObserver(
			(entries) => {
				for (const entry of entries) {
					if (entry.isIntersecting) {
						entry.target.classList.add('is-visible');
						observer.unobserve(entry.target);
					}
				}
			},
			{ threshold: 0.2 }
		);

		rows.forEach((row) => observer.observe(row));
		return () => observer.disconnect();
	});

	function groupStyle(title: string) {
		const theme = groupThemes[title];
		return `--row-pastel: ${theme.pastel}; --row-accent: ${theme.accent}; --row-label: ${theme.label};`;
	}

	function chipStyle(skill: string, index: number) {
		const theme = chipThemes[skill];
		return `--chip-accent: ${theme.background}; --chip-text: ${theme.text}; --chip-index: ${index};`;
	}
</script>

<div class="skills-tree" bind:this={skillsTree}>
	{#each skills as group (group.title)}
		<div class="skill-row" style={groupStyle(group.title)}>
			<h3>{group.title}</h3>
			<ul aria-label={group.title}>
				{#each group.items as skill, index (skill)}
					<li class="tree-chip" style={chipStyle(skill, index)}>
						<span class="chip-icon"><SkillIcon name={skill} /></span>
						<span>{skill}</span>
					</li>
				{/each}
			</ul>
		</div>
	{/each}
</div>

<style>
	.skill-row {
		--chip-line: var(--ink);
		--chip-fill: var(--row-pastel);
		--chip-shadow: var(--ink);
		--label-color: var(--row-label);
		position: relative;
		display: grid;
		grid-template-columns: 170px minmax(0, 1fr);
		gap: 16px;
		padding: 22px 0 24px;
		align-items: start;
	}
	.skill-row::after {
		content: '';
		position: absolute;
		left: 0;
		right: 0;
		bottom: 0;
		height: 1px;
		background: var(--line);
		transform: scaleX(0);
		transform-origin: left;
		transition: transform 0.9s cubic-bezier(0.6, 0, 0.2, 1);
	}
	.skill-row:global(.is-visible)::after {
		transform: none;
	}
	:global(html[data-theme='dark']) .skill-row {
		--chip-line: var(--row-accent);
		--chip-fill: var(--white);
		--chip-shadow: var(--row-accent);
		--label-color: var(--row-accent);
	}
	h3 {
		color: var(--label-color);
		font-size: 16px;
		line-height: 1.2;
		margin: 7px 0 0;
		letter-spacing: -0.3px;
	}
	ul {
		display: flex;
		flex-wrap: wrap;
		gap: 12px 14px;
		list-style: none;
		padding: 0;
		margin: 0;
		min-width: 0;
	}
	.tree-chip {
		position: relative;
		isolation: isolate;
		overflow: hidden;
		display: inline-flex;
		align-items: center;
		gap: 9px;
		max-width: 100%;
		padding: 6px 13px 6px 7px;
		border: 2px solid var(--chip-line);
		border-radius: 7px;
		background: var(--chip-fill);
		color: var(--skill-chip-ink);
		box-shadow: 4px 4px 0 var(--chip-shadow);
		font: 600 12px/1.5 var(--mono);
		overflow-wrap: anywhere;
		cursor: default;
		user-select: none;
		transition:
			transform 0.2s cubic-bezier(0.3, 1.7, 0.5, 1),
			box-shadow 0.2s,
			color 0.25s;
		animation: chip-pop 0.55s cubic-bezier(0.2, 1.5, 0.4, 1) backwards paused;
		animation-delay: calc(var(--chip-index) * 55ms);
	}
	.skill-row:global(.is-visible) .tree-chip {
		animation-play-state: running;
	}
	.tree-chip::before {
		content: '';
		position: absolute;
		z-index: -1;
		inset: 0;
		background: var(--chip-accent);
		transform: scaleX(0);
		transform-origin: left;
		transition: transform 0.32s cubic-bezier(0.7, 0, 0.2, 1);
	}
	.tree-chip::after {
		content: '';
		position: absolute;
		top: 0;
		bottom: 0;
		left: -40%;
		width: 30%;
		background: linear-gradient(100deg, transparent, rgba(255, 255, 255, 0.55), transparent);
		transform: skewX(-20deg);
		pointer-events: none;
	}
	.tree-chip:hover {
		transform: translate(-2px, -3px);
		box-shadow: 7px 7px 0 var(--chip-shadow);
		color: var(--chip-text);
		outline: 0;
	}
	.tree-chip:hover::before {
		transform: none;
	}
	.tree-chip:hover::after {
		left: 120%;
		transition: left 0.6s ease;
	}
	.tree-chip:active {
		transform: translate(3px, 3px);
		box-shadow: 1px 1px 0 var(--chip-shadow);
	}
	.chip-icon {
		display: grid;
		place-items: center;
		flex: 0 0 29px;
		width: 29px;
		height: 29px;
		border: 2px solid var(--chip-line);
		border-radius: 5px;
		background: var(--chip-accent);
		color: var(--chip-text);
		transition:
			transform 0.35s cubic-bezier(0.3, 1.9, 0.5, 1),
			background 0.25s,
			color 0.25s;
	}
	.tree-chip:hover .chip-icon {
		transform: rotate(-14deg) scale(1.2);
		background: var(--ink);
		color: var(--paper);
	}
	@keyframes chip-pop {
		from {
			opacity: 0;
			transform: translateY(16px) scale(0.85) rotate(-3deg);
		}
	}
	@media (max-width: 650px) {
		.skill-row {
			grid-template-columns: 1fr;
			gap: 10px;
		}
		h3 {
			margin: 0;
		}
	}
	@media (prefers-reduced-motion: reduce) {
		.skill-row::after,
		.tree-chip,
		.tree-chip::before,
		.tree-chip::after,
		.chip-icon {
			animation: none;
			transition: none;
		}
		.tree-chip:hover,
		.tree-chip:active,
		.tree-chip:hover .chip-icon {
			transform: none;
		}
	}
</style>
