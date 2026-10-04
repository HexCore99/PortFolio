<script lang="ts">
	import { reveal } from '#lib/reveal.js';
	import { NeoButton } from '@dvcol/neo-svelte/buttons';
	import type { Project } from '#lib/data/portfolio.js';
	import ProjectVisual from './ProjectVisual.svelte';
	import Icon from './Icon.svelte';
	let { project, compact = false }: { project: Project; compact?: boolean } = $props();
</script>

<article
	use:reveal
	class="project-card"
	class:featured={project.featured}
	class:compact
	aria-labelledby={`project-${project.id}`}
>
	<div class="visual-wrap"><ProjectVisual {project} {compact} /></div>
	<div class="project-copy">
		<p class="project-category">
			{#if project.featured}<span class="featured-dot"></span> FEATURED PROJECT{:else}{project.category}{/if}
		</p>
		<h3 id={`project-${project.id}`}>{project.title}</h3>
		<p class="summary">{project.summary}</p>
		{#if project.detail}<p class="detail">{project.detail}</p>{/if}
		<ul class="tags" aria-label={`${project.title} technologies`}>
			{#each project.tags as tag (tag)}
				<li class="project-tag">{tag}</li>
			{/each}
		</ul>
		<div class="project-links">
			<NeoButton
				elevation={0}
				hover={0}
				active={0}
				scale={false}
				class="button button-secondary"
				href={project.repositoryUrl}
				{...{ target: '_blank', rel: 'noreferrer' }}
				aria-label={`${project.title} GitHub source (opens in a new tab)`}
				><Icon name="github" size={16} /> GitHub source <Icon name="arrow" size={15} /></NeoButton
			>{#if project.releaseUrl}<NeoButton
					elevation={0}
					hover={0}
					active={0}
					scale={false}
					class="button button-primary"
					href={project.releaseUrl}
					{...{ target: '_blank', rel: 'noreferrer' }}
					aria-label={`${project.title} latest release (opens in a new tab)`}
					>Latest release <Icon name="arrow" size={15} /></NeoButton
				>{/if}
		</div>
	</div>
</article>

<style>
	.project-card {
		display: flex;
		flex-direction: column;
		border: 1.5px solid var(--ink);
		border-radius: 10px;
		overflow: hidden;
		background: var(--white);
		box-shadow: 0 4px 0 #182a4125;
	}
	.project-copy {
		min-width: 0;
		padding: 29px;
		display: flex;
		flex-direction: column;
		flex: 1;
	}
	.project-category {
		font: 600 11px/1.6 var(--mono);
		text-transform: uppercase;
		letter-spacing: 1px;
		color: var(--muted);
		margin-bottom: 14px;
		display: flex;
		align-items: center;
		gap: 8px;
	}
	h3 {
		text-wrap: balance;
		font-size: 28px;
		font-weight: 750;
		line-height: 1.13;
		letter-spacing: -1px;
		margin-bottom: 14px;
	}
	.summary {
		font-size: 15px;
		font-weight: 600;
		line-height: 1.65;
	}
	.detail {
		font-size: 14px;
		line-height: 1.8;
		color: var(--muted);
		margin-top: 12px;
	}
	.tags {
		list-style: none;
		padding: 0;
		display: flex;
		flex-wrap: wrap;
		gap: 7px;
		margin: 24px 0 26px;
	}
	.project-tag {
		max-width: 100%;
		overflow-wrap: anywhere;
		padding: 4px 8px;
		border-radius: 2px;
		background: #eaf0f1;
		color: #42586a;
		font: 500 11px/1.5 var(--mono);
	}
	.featured .project-tag {
		background: #293e53;
		color: #dce6f1;
	}
	.project-links {
		--button-size: 12px;
		--button-padding: 11px 14px;
		margin-top: auto;
		display: flex;
		flex-wrap: wrap;
		gap: 13px;
		padding-top: 20px;
		border-top: 1px solid var(--line);
	}
	.project-links :global(.button) {
		min-height: 45px;
		font-size: 12px;
		gap: 9px;
		padding: 11px 14px;
		border-width: 1.5px;
		box-shadow: none;
		border-radius: 5px;
	}
	.project-links :global(.button):hover {
		box-shadow: 0 3px 0 #182a4130;
	}
	.project-links :global(.button):active {
		box-shadow: none;
	}
	.featured {
		display: grid;
		grid-template-columns: 0.85fr 1.15fr;
		background: var(--ink);
		color: var(--cream);
	}
	.featured .visual-wrap {
		grid-column: 2;
		grid-row: 1;
		display: grid;
		border-left: 1.5px solid var(--ink);
	}
	.featured .project-copy {
		grid-column: 1;
		grid-row: 1;
		padding: 35px;
	}
	.featured h3 {
		font-size: 45px;
		letter-spacing: -1.8px;
	}
	.featured .project-category {
		color: var(--coral);
	}
	.featured .detail {
		color: #c0ccdb;
	}
	.featured .project-links {
		border-top-color: #536075;
	}
	.featured :global(a:focus-visible) {
		outline-color: var(--coral);
	}
	.featured .featured-dot {
		width: 6px;
		height: 6px;
		background: var(--coral);
	}
	.compact {
		display: grid;
		grid-template-rows: auto 1fr;
		grid-template-columns: minmax(0, 1fr);
	}
	.compact .visual-wrap {
		display: grid;
		height: 230px;
		border-bottom: 1px solid #c3ccd2;
	}
	.compact .project-copy {
		padding: 24px;
	}
	.compact h3 {
		font-size: 21px;
	}
	.compact .summary {
		font-size: 14px;
		font-weight: 400;
		color: var(--muted);
	}
	.compact .tags {
		margin: 18px 0;
	}
	.compact .project-category {
		font-size: 10px;
	}
	@media (max-width: 1100px) {
		.featured .project-copy {
			padding: 28px;
		}
		.compact {
			grid-template-columns: 1fr;
		}
		.compact .visual-wrap {
			max-height: 190px;
			border-right: 0;
			border-bottom: 1px solid #c3ccd2;
		}
	}
	@media (max-width: 800px) {
		.featured {
			display: flex;
			flex-direction: column;
		}
		.featured .visual-wrap {
			border-left: 0;
			border-bottom: 1.5px solid var(--ink);
		}
		.project-copy {
			padding: 23px;
		}
		.featured .project-copy {
			padding: 28px;
		}
		.featured h3 {
			font-size: 36px;
		}
	}
	@media (max-width: 600px) {
		.compact .visual-wrap {
			max-height: none;
		}
		.project-copy {
			padding: 23px;
		}
		.project-links :global(.button) {
			min-height: 46px;
			font-size: 12px;
		}
	}

	.project-card {
		transition:
			translate 0.3s ease,
			box-shadow 0.3s ease,
			border-color 0.3s ease;
	}
	.visual-wrap :global(img),
	.visual-wrap :global(svg) {
		transition: scale 0.6s cubic-bezier(0.2, 0.7, 0.2, 1);
	}
	@media (hover: hover) and (pointer: fine) {
		.project-card:hover {
			translate: 0 -7px;
			box-shadow: 0 14px 26px #182a411c;
			border-color: var(--blue);
		}
		.project-card:hover .visual-wrap :global(img),
		.project-card:hover .visual-wrap :global(svg) {
			scale: 1.035;
		}
	}
	.project-card:focus-within {
		box-shadow: 0 8px 20px #182a4120;
		border-color: var(--blue);
	}
	@media (prefers-reduced-motion: reduce) {
		.project-card:hover {
			translate: none;
		}
		.project-card:hover .visual-wrap :global(img),
		.project-card:hover .visual-wrap :global(svg) {
			scale: 1;
		}
	}
</style>
