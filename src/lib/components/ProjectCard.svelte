<script lang="ts">
	import type { Project } from '#lib/data/portfolio.js';
	import ProjectVisual from './ProjectVisual.svelte';
	import Icon from './Icon.svelte';
	let { project, compact = false }: { project: Project; compact?: boolean } = $props();
</script>

<article
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
			{#each project.tags as tag (tag)}<li>{tag}</li>{/each}
		</ul>
		<div class="project-links">
			<a
				href={project.repositoryUrl}
				target="_blank"
				rel="noreferrer"
				aria-label={`${project.title} GitHub source (opens in a new tab)`}
				><Icon name="github" size={16} /> GitHub source <Icon name="arrow" size={15} /></a
			>{#if project.releaseUrl}<a
					href={project.releaseUrl}
					target="_blank"
					rel="noreferrer"
					aria-label={`${project.title} latest release (opens in a new tab)`}
					>Latest release <Icon name="arrow" size={15} /></a
				>{/if}
		</div>
	</div>
</article>

<style>
	.project-card {
		display: flex;
		flex-direction: column;
		border: 2px solid var(--ink);
		border-radius: 4px;
		overflow: hidden;
		background: var(--white);
		box-shadow: 5px 5px 0 var(--ink);
		transition:
			transform 0.15s,
			box-shadow 0.15s;
	}
	.project-card:hover {
		transform: translateY(-2px);
		box-shadow: 5px 7px 0 var(--ink);
	}
	.project-copy {
		padding: 27px;
		display: flex;
		flex-direction: column;
		flex: 1;
	}
	.project-category {
		font: 700 9px var(--mono);
		text-transform: uppercase;
		letter-spacing: 1.2px;
		color: var(--muted);
		margin-bottom: 12px;
		display: flex;
		align-items: center;
		gap: 7px;
	}
	h3 {
		font-size: 27px;
		font-weight: 900;
		text-transform: uppercase;
		line-height: 1.08;
		letter-spacing: -1px;
		margin-bottom: 14px;
	}
	.summary {
		font-size: 14px;
		font-weight: 700;
		line-height: 1.6;
		color: var(--ink);
	}
	.detail {
		font-size: 13px;
		line-height: 1.8;
		color: #4f4439;
		margin-top: 11px;
	}
	.tags {
		list-style: none;
		padding: 0;
		display: flex;
		flex-wrap: wrap;
		gap: 6px;
		margin: 21px 0 24px;
	}
	.tags li {
		background: var(--paper);
		border: 1px solid var(--ink);
		padding: 4px 7px;
		border-radius: 2px;
		color: var(--ink);
		font: 9px var(--mono);
		line-height: 1.4;
	}
	.project-links {
		margin-top: auto;
		display: flex;
		flex-wrap: wrap;
		gap: 12px;
		padding-top: 18px;
		border-top: 1px solid #9b8d72;
	}
	.project-links a {
		display: inline-flex;
		align-items: center;
		gap: 7px;
		text-decoration: none;
		text-transform: uppercase;
		font: 700 9px var(--mono);
		min-height: 37px;
		background: var(--stone);
		color: white;
		border: 2px solid var(--ink);
		box-shadow: 2px 2px 0 var(--ink);
		border-radius: 3px;
		padding: 8px 10px;
		transition:
			transform 0.15s,
			box-shadow 0.15s;
	}
	.project-links a + a {
		background: var(--mustard);
		color: var(--ink);
	}
	.project-links a:hover {
		transform: translate(1px, 1px);
		box-shadow: 1px 1px 0 var(--ink);
	}
	.featured {
		display: grid;
		grid-template-columns: 0.85fr 1.15fr;
		background: var(--mauve);
	}
	.featured .visual-wrap {
		grid-column: 2;
		grid-row: 1;
		display: grid;
		border-left: 2px solid var(--ink);
	}
	.featured .project-copy {
		grid-column: 1;
		grid-row: 1;
		padding: 33px;
	}
	.featured h3 {
		font-size: 43px;
		letter-spacing: -1.8px;
	}
	.featured .project-category,
	.featured .detail {
		color: #171015;
	}
	.featured .project-links {
		border-top-color: #743b56;
	}
	.featured-dot {
		width: 7px;
		height: 7px;
		background: var(--mustard);
		border: 1px solid var(--ink);
	}
	.compact {
		display: grid;
		grid-template-columns: 135px 1fr;
	}
	.compact .visual-wrap {
		display: grid;
		border-right: 2px solid var(--ink);
	}
	.compact .project-copy {
		padding: 22px;
	}
	.compact h3 {
		font-size: 20px;
	}
	.compact .summary {
		font-size: 12px;
		font-weight: 400;
	}
	.compact .tags {
		margin: 15px 0;
	}
	.compact .project-category {
		font-size: 8px;
	}
	@media (max-width: 1000px) {
		.featured .project-copy {
			padding: 25px;
		}
		.compact {
			grid-template-columns: 1fr;
		}
		.compact .visual-wrap {
			max-height: 175px;
			border-right: 0;
			border-bottom: 2px solid var(--ink);
		}
	}
	@media (max-width: 800px) {
		.featured {
			display: flex;
			flex-direction: column;
		}
		.featured .visual-wrap {
			border-left: 0;
			border-bottom: 2px solid var(--ink);
		}
		.project-copy {
			padding: 23px;
		}
		.featured .project-copy {
			padding: 26px;
		}
		.featured h3 {
			font-size: 36px;
		}
	}
	@media (max-width: 600px) {
		.compact .visual-wrap {
			max-height: none;
		}
	}
</style>
