<script lang="ts">
	import { onMount } from 'svelte';
	import SectionHeading from './SectionHeading.svelte';
	import SkillIcon from './SkillIcon.svelte';

	type CategoryName =
		'Languages' | 'Frontend' | 'Backend and data' | 'Machine learning' | 'Desktop and tools';

	type Skill = {
		name: string;
		category: CategoryName;
		accent: string;
		text: string;
		projects: string[];
	};

	type ProjectTheme = { id: string; color: string };
	type CategoryTheme = {
		name: CategoryName;
		color: string;
		darkColor: string;
		darkFill: string;
	};

	const categories: CategoryTheme[] = [
		{
			name: 'Languages',
			color: '#f2cdb0',
			darkColor: '#f0a979',
			darkFill: '#34241f'
		},
		{ name: 'Frontend', color: '#c8dfc9', darkColor: '#7fd1a0', darkFill: '#1f3029' },
		{
			name: 'Backend and data',
			color: '#c9daf0',
			darkColor: '#7fb2f0',
			darkFill: '#1e2b3b'
		},
		{
			name: 'Machine learning',
			color: '#dccbea',
			darkColor: '#c29bf0',
			darkFill: '#30243a'
		},
		{
			name: 'Desktop and tools',
			color: '#f1dfa4',
			darkColor: '#f0cf6b',
			darkFill: '#332f20'
		}
	];

	const projectThemes: Record<string, ProjectTheme> = {
		Taskora: { id: 'project-taskora', color: '#b7b9ff' },
		WhoLocks: { id: 'project-wholocks', color: '#ff5d8f' },
		QuickJudge: { id: 'project-quickjudge', color: '#ffd23f' },
		HexSolve: { id: 'project-hexsolve', color: '#9fd8cb' },
		Recommender: { id: 'project-movies', color: '#ffb98a' },
		Snake: { id: 'project-snake', color: '#c9f27a' },
		Clock: { id: 'project-clock', color: '#f5a8ff' }
	};

	const darkText = '#14213d';
	const lightText = '#ffffff';
	const skillRows: Skill[][] = [
		[
			{
				name: 'Rust',
				category: 'Languages',
				accent: '#f26b3a',
				text: darkText,
				projects: ['Taskora', 'WhoLocks']
			}
		],
		[
			{
				name: 'React',
				category: 'Frontend',
				accent: '#61dafb',
				text: darkText,
				projects: ['Taskora', 'QuickJudge']
			},
			{
				name: 'Zustand',
				category: 'Frontend',
				accent: '#f0a53a',
				text: darkText,
				projects: ['Taskora']
			},
			{
				name: 'Redux Toolkit',
				category: 'Frontend',
				accent: '#764abc',
				text: lightText,
				projects: ['QuickJudge']
			}
		],
		[
			{
				name: 'Tauri 2',
				category: 'Desktop and tools',
				accent: '#ffc131',
				text: darkText,
				projects: ['Taskora']
			},
			{
				name: 'SQLite',
				category: 'Backend and data',
				accent: '#4aa3d8',
				text: darkText,
				projects: ['Taskora']
			}
		],
		[
			{
				name: 'Express',
				category: 'Backend and data',
				accent: '#b8bec9',
				text: darkText,
				projects: ['QuickJudge']
			},
			{
				name: 'MySQL',
				category: 'Backend and data',
				accent: '#4479a1',
				text: lightText,
				projects: ['QuickJudge']
			},
			{
				name: 'JWT',
				category: 'Backend and data',
				accent: '#fb015b',
				text: lightText,
				projects: ['QuickJudge']
			}
		],
		[
			{
				name: 'Python',
				category: 'Languages',
				accent: '#4b8bbe',
				text: lightText,
				projects: ['Recommender']
			},
			{
				name: 'Flask',
				category: 'Backend and data',
				accent: '#34d399',
				text: darkText,
				projects: ['Recommender']
			},
			{
				name: 'TensorFlow/Keras',
				category: 'Machine learning',
				accent: '#ff8f00',
				text: darkText,
				projects: ['Recommender']
			},
			{
				name: 'Next.js',
				category: 'Frontend',
				accent: '#e8e8e8',
				text: darkText,
				projects: ['Recommender']
			}
		],
		[
			{
				name: 'Tailwind CSS',
				category: 'Frontend',
				accent: '#38bdf8',
				text: darkText,
				projects: []
			},
			{
				name: 'Vite',
				category: 'Frontend',
				accent: '#a78bfa',
				text: darkText,
				projects: []
			},
			{
				name: 'React Router',
				category: 'Frontend',
				accent: '#ef4444',
				text: lightText,
				projects: []
			}
		],
		[
			{
				name: 'C++',
				category: 'Languages',
				accent: '#00599c',
				text: lightText,
				projects: ['HexSolve', 'Snake', 'Clock']
			},
			{
				name: 'raylib',
				category: 'Desktop and tools',
				accent: '#f2f2f2',
				text: darkText,
				projects: ['Snake', 'Clock']
			}
		],
		[
			{
				name: 'CLI tools',
				category: 'Desktop and tools',
				accent: '#9be564',
				text: darkText,
				projects: ['WhoLocks']
			},
			{
				name: 'Windows file-system tooling',
				category: 'Desktop and tools',
				accent: '#00a4ef',
				text: darkText,
				projects: ['WhoLocks']
			}
		],
		[
			{
				name: 'C',
				category: 'Languages',
				accent: '#6a7bd6',
				text: lightText,
				projects: ['HexSolve']
			},
			{ name: 'Java', category: 'Languages', accent: '#f89820', text: darkText, projects: [] },
			{
				name: 'JavaScript',
				category: 'Languages',
				accent: '#f7df1e',
				text: darkText,
				projects: []
			},
			{
				name: 'TypeScript',
				category: 'Languages',
				accent: '#3178c6',
				text: lightText,
				projects: []
			},
			{
				name: 'SvelteKit',
				category: 'Frontend',
				accent: '#ff3e00',
				text: darkText,
				projects: []
			},
			{
				name: 'SDL3',
				category: 'Desktop and tools',
				accent: '#3a8fd6',
				text: lightText,
				projects: []
			}
		]
	];

	let skillsTable: HTMLDivElement;
	let highlightedProjects = $state<string[] | null>(null);

	function highlight(projects: string[]) {
		highlightedProjects = projects;
	}

	function clearHighlight() {
		highlightedProjects = null;
	}

	onMount(() => {
		const rows = skillsTable.querySelectorAll<HTMLElement>('.project-row');
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

	function categoryTheme(category: CategoryName) {
		return categories.find((item) => item.name === category) ?? categories[0];
	}

	function rowProjects(row: Skill[]) {
		return [...new Set(row.flatMap((skill) => skill.projects))];
	}

	function skillStyle(skill: Skill, index: number) {
		const category = categoryTheme(skill.category);
		return `--chip-accent: ${skill.accent}; --chip-text: ${skill.text}; --category-color: ${category.color}; --category-dark-color: ${category.darkColor}; --category-dark-fill: ${category.darkFill}; --chip-index: ${index};`;
	}

	function projectStyle(project: string, index: number) {
		return `--project-color: ${projectThemes[project].color}; --project-index: ${index};`;
	}
</script>

<div class="skills-layout">
	<div class="skills-rail">
		<SectionHeading id="about-title" title="Skills" />
		<ul class="legend" aria-label="Skill categories">
			{#each categories as category (category.name)}
				<li
					style={`--category-color: ${category.color}; --category-dark-color: ${category.darkColor};`}
				>
					<span aria-hidden="true"></span>{category.name}
				</li>
			{/each}
		</ul>
	</div>

	<div class="skills-table" bind:this={skillsTable}>
		<div class="table-heading" aria-hidden="true">
			<span>Skill (hover one)</span><span>Where I used it</span>
		</div>
		{#each skillRows as row, rowIndex (rowIndex)}
			{@const projects = rowProjects(row)}
			<div class="project-row">
				<ul class="skill-list" aria-label={`Skill group ${rowIndex + 1}`}>
					{#each row as skill, index (skill.name)}
						<li>
							<button
								type="button"
								class="skill-chip"
								style={skillStyle(skill, index)}
								aria-label={`Highlight projects using ${skill.name}`}
								onpointerenter={() => highlight(skill.projects)}
								onpointerleave={clearHighlight}
								onfocus={() => highlight(skill.projects)}
								onblur={clearHighlight}
							>
								<span class="skill-icon"><SkillIcon name={skill.name} /></span>
								<span>{skill.name}</span>
							</button>
						</li>
					{/each}
				</ul>

				{#if projects.length}
					<div class="project-list" aria-label="Projects using these skills">
						{#each projects as project, index (project)}
							<a
								href={`#${projectThemes[project].id}`}
								style={projectStyle(project, index)}
								class:dimmed={highlightedProjects !== null &&
									!highlightedProjects.includes(project)}>{project}</a
							>
						{/each}
					</div>
				{:else}
					<p class="no-project">Also used. Not in a featured project yet.</p>
				{/if}
			</div>
		{/each}
	</div>
</div>

<style>
	.skills-layout {
		display: grid;
		grid-template-columns: 200px minmax(0, 1fr);
		gap: 40px;
		align-items: start;
	}
	.skills-rail {
		position: sticky;
		top: 120px;
		align-self: start;
	}
	.skills-rail :global(.section-heading) {
		margin: 0 0 20px;
	}
	.skills-rail :global(h2) {
		max-width: 180px;
		font-size: 34px;
		line-height: 1.12;
		letter-spacing: -1.3px;
	}
	.legend {
		display: grid;
		gap: 9px;
		margin: 0;
		padding: 0;
		list-style: none;
		color: var(--muted);
		font: 400 11px/1.4 var(--mono);
	}
	.legend li {
		display: flex;
		align-items: center;
		gap: 8px;
		font-weight: 500;
	}
	.legend li > span {
		width: 14px;
		height: 14px;
		border: 2px solid var(--ink);
		border-radius: 4px;
		background: var(--category-color);
		box-shadow: 2px 2px 0 var(--ink);
	}
	:global(html[data-theme='dark']) .legend li {
		color: var(--category-dark-color);
	}
	:global(html[data-theme='dark']) .legend li > span {
		border-color: var(--category-dark-color);
		background: var(--category-dark-color);
		box-shadow: 2px 2px 0 color-mix(in srgb, var(--category-dark-color) 45%, transparent);
	}
	.skills-table {
		min-width: 0;
	}
	.table-heading,
	.project-row {
		display: grid;
		grid-template-columns: minmax(0, 1.7fr) minmax(0, 1fr);
		gap: 20px;
		align-items: center;
	}
	.table-heading {
		padding: 0 0 10px;
		border-bottom: 1px solid var(--line);
		color: var(--muted);
		font: 400 12px/1.4 var(--mono);
	}
	.project-row {
		position: relative;
		padding: 20px 0 22px;
	}
	.project-row::after {
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
	.project-row:global(.is-visible)::after {
		transform: none;
	}
	.skill-list,
	.project-list {
		display: flex;
		flex-wrap: wrap;
		gap: 10px 12px;
		margin: 0;
		padding: 0;
		list-style: none;
	}
	.skill-chip {
		--chip-line: var(--ink);
		--chip-shadow: var(--ink);
		--chip-fill: var(--category-color);
		position: relative;
		isolation: isolate;
		overflow: hidden;
		display: inline-flex;
		align-items: center;
		gap: 8px;
		padding: 5px 12px 5px 6px;
		border: 2px solid var(--chip-line);
		border-radius: 7px;
		background: var(--chip-fill);
		color: #14213d;
		box-shadow: 3px 3px 0 var(--chip-shadow);
		font: 500 12px/1.4 var(--mono);
		cursor: default;
		user-select: none;
		transition:
			transform 0.2s cubic-bezier(0.3, 1.7, 0.5, 1),
			box-shadow 0.2s,
			color 0.25s;
		animation: chip-pop 0.55s cubic-bezier(0.2, 1.5, 0.4, 1) backwards paused;
		animation-delay: calc(var(--chip-index) * 45ms);
	}
	:global(html[data-theme='dark']) .skill-chip {
		--chip-line: var(--category-dark-color);
		--chip-shadow: var(--category-dark-color);
		--chip-fill: var(--category-dark-fill);
		color: var(--ink);
	}
	.project-row:global(.is-visible) .skill-chip,
	.project-row:global(.is-visible) .project-list a {
		animation-play-state: running;
	}
	.skill-chip::before {
		content: '';
		position: absolute;
		z-index: -1;
		inset: 0;
		background: var(--chip-accent);
		transform: scaleX(0);
		transform-origin: left;
		transition: transform 0.32s cubic-bezier(0.7, 0, 0.2, 1);
	}
	.skill-chip::after {
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
	.skill-chip:hover,
	.skill-chip:focus-visible {
		transform: translate(-2px, -3px);
		box-shadow: 6px 6px 0 var(--chip-shadow);
		color: var(--chip-text);
		outline: 0;
	}
	.skill-chip:hover::before,
	.skill-chip:focus-visible::before {
		transform: none;
	}
	.skill-chip:hover::after,
	.skill-chip:focus-visible::after {
		left: 120%;
		transition: left 0.6s ease;
	}
	.skill-chip:active {
		transform: translate(2px, 2px);
		box-shadow: 1px 1px 0 var(--chip-shadow);
	}
	.skill-icon {
		--skill-background: var(--chip-accent);
		display: grid;
		place-items: center;
		min-width: 28px;
		height: 28px;
		padding: 0 2px;
		border: 2px solid var(--chip-line);
		border-radius: 5px;
		background: var(--chip-accent);
		color: var(--chip-text);
		transition:
			transform 0.35s cubic-bezier(0.3, 1.9, 0.5, 1),
			background 0.25s,
			color 0.25s;
	}
	.skill-chip:hover .skill-icon,
	.skill-chip:focus-visible .skill-icon {
		transform: rotate(-14deg) scale(1.18);
		border-color: #14213d;
		background: #fffdf7;
		color: #14213d;
	}
	.project-list a {
		padding: 3px 10px;
		border: 2px solid var(--ink);
		border-radius: 5px;
		background: var(--project-color);
		color: #14213d;
		box-shadow: 2px 2px 0 var(--ink);
		font: 500 11px/1.5 var(--mono);
		text-decoration: none;
		animation: chip-pop 0.5s cubic-bezier(0.2, 1.5, 0.4, 1) backwards paused;
		animation-delay: calc(280ms + var(--project-index) * 70ms);
		transition:
			transform 0.15s,
			box-shadow 0.15s,
			opacity 0.2s,
			filter 0.2s;
	}
	.project-list a:hover,
	.project-list a:focus-visible {
		transform: translateY(-2px);
		box-shadow: 4px 4px 0 var(--ink);
	}
	.project-list a.dimmed {
		opacity: 0.2;
		filter: grayscale(1);
		transform: scale(0.94);
	}
	.no-project {
		margin: 0;
		color: var(--muted);
		font: 400 12px/1.5 var(--mono);
	}
	@keyframes chip-pop {
		from {
			opacity: 0;
			transform: translateY(14px) scale(0.85) rotate(-3deg);
		}
	}
	@media (max-width: 1100px) {
		.skills-layout {
			grid-template-columns: 1fr;
			gap: 28px;
		}
		.skills-rail {
			position: static;
		}
		.skills-rail :global(h2) {
			max-width: none;
			font-size: 36px;
		}
		.legend {
			grid-template-columns: repeat(3, max-content);
			gap: 9px 20px;
		}
	}
	@media (max-width: 700px) {
		.skills-rail :global(h2) {
			font-size: 32px;
		}
		.legend {
			grid-template-columns: repeat(2, minmax(0, max-content));
		}
		.table-heading {
			display: none;
		}
		.project-row {
			grid-template-columns: 1fr;
			gap: 12px;
		}
	}
	@media (prefers-reduced-motion: reduce) {
		.project-row::after,
		.skill-chip,
		.skill-chip::before,
		.skill-chip::after,
		.skill-icon,
		.project-list a {
			animation: none;
			transition: none;
		}
		.skill-chip:hover,
		.skill-chip:focus-visible,
		.skill-chip:active,
		.skill-chip:hover .skill-icon,
		.skill-chip:focus-visible .skill-icon,
		.project-list a:hover,
		.project-list a:focus-visible,
		.project-list a.dimmed {
			transform: none;
		}
	}
</style>
