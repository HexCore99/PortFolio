<script lang="ts">
	import { resolve } from '$app/paths';
	import ProjectCard from '#lib/components/ProjectCard.svelte';
	import { projects } from '#lib/data/portfolio.js';
</script>

<svelte:head>
	<title>Other Projects — Siabul Hassan</title>
	<meta name="description" content="Explore more projects by Siabul Hassan." />
</svelte:head>

<main class="container section">
	<a class="button button-secondary" href={resolve('/#work')}>← Back to Top Work</a>
	<h1>Other Projects</h1>
	<div class="catalog">
		{#each projects.filter((project) => project.additional && !project.featured) as project (project.id)}
			<ProjectCard {project} compact />
		{/each}
	</div>
</main>

<style>
	h1 {
		margin-block: 32px;
		font-size: clamp(2.5rem, 6vw, 4rem);
		line-height: 1.1;
	}
	.catalog {
		display: grid;
		grid-template-columns: repeat(2, minmax(0, 1fr));
		gap: 25px;
	}
	@media (max-width: 740px) {
		.catalog {
			grid-template-columns: 1fr;
		}
	}
</style>
