<script lang="ts">
	import Navigation from '#lib/components/Navigation.svelte';
	import Hero from '#lib/components/Hero.svelte';
	import SectionHeading from '#lib/components/SectionHeading.svelte';
	import SkillsBlock from '#lib/components/SkillsBlock.svelte';
	import ProjectCard from '#lib/components/ProjectCard.svelte';
	import Footer from '#lib/components/Footer.svelte';
	import { projects } from '#lib/data/portfolio.js';
	import { asset } from '$app/paths';
	const description =
		'Siabul Hassan builds practical software across web, desktop, and systems. Explore Taskora, WhoLocks, full-stack applications, and C++ projects.';
</script>

<svelte:head>
	<title>Siabul Hassan — Full-Stack Developer</title>
	<meta name="description" content={description} />
	<meta name="theme-color" content="#f6f3ea" />
	<meta property="og:title" content="Siabul Hassan — Full-Stack Developer" />
	<meta property="og:description" content={description} />
	<meta property="og:type" content="website" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:image" content={asset('social-preview.png')} />
	<meta property="og:image:width" content="1200" />
	<meta property="og:image:height" content="630" />
	<meta
		property="og:image:alt"
		content="Siabul Hassan — Software Developer. Building useful software across web, desktop, and systems."
	/>
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:title" content="Siabul Hassan — Full-Stack Developer" />
	<meta name="twitter:description" content={description} />
	<meta name="twitter:image" content={asset('social-preview.png')} />
	<meta
		name="twitter:image:alt"
		content="Siabul Hassan — Software Developer. Building useful software across web, desktop, and systems."
	/>
</svelte:head>

<div id="top"></div>
<a class="skip-link" href="#main">Skip to content</a>
<Navigation />
<main id="main" tabindex="-1">
	<Hero />
	<section id="about" class="section about-section container" aria-labelledby="about-title">
		<div class="about-grid">
			<SectionHeading id="about-title" title="A practical approach" />
			<div class="about-copy">
				<p>
					I’m Siabul, a software developer who enjoys working across the stack—from the interface
					you interact with to the systems that make it work.
				</p>
				<p>
					My projects span local-first productivity tools, Windows utilities, full-stack platforms,
					and machine learning. The common thread: a concrete problem, a considered interface, and
					an implementation I can build on.
				</p>
			</div>
		</div>
		<SkillsBlock />
	</section>
	<section id="work" class="work-section section" aria-labelledby="work-title">
		<div class="container">
			<SectionHeading
				id="work-title"
				title="Selected work"
				description="A closer look at the things I build. Practical problems, explored across different stacks."
			/>
			{#each projects.filter((project) => project.featured) as project (project.id)}<ProjectCard
					{project}
				/>{/each}
			<div class="project-grid">
				{#each projects.filter((project) => !project.featured && !project.additional) as project (project.id)}<ProjectCard
						{project}
					/>{/each}
			</div>
		</div>
	</section>
	<section class="section additional-section container" aria-labelledby="additional-title">
		<SectionHeading
			id="additional-title"
			title="Additional builds"
			description="Smaller projects. The same curiosity for how things work."
		/>
		<div class="additional-grid">
			{#each projects.filter((project) => project.additional) as project (project.id)}<ProjectCard
					{project}
					compact
				/>{/each}
		</div>
	</section>
</main>
<Footer />

<style>
	.about-grid {
		display: grid;
		grid-template-columns: 1fr 1.1fr;
		gap: 65px;
	}
	.about-copy {
		padding-top: 4px;
	}
	.about-copy p:first-child {
		font-size: 19px;
		line-height: 1.7;
		letter-spacing: -0.4px;
	}
	.about-copy p + p {
		margin-top: 18px;
		font-size: 14px;
		line-height: 1.9;
		color: var(--muted);
	}
	.work-section {
		background: #edf0ea;
		border-block: 1px solid var(--line);
	}
	.project-grid {
		display: grid;
		grid-template-columns: repeat(2, minmax(0, 1fr));
		gap: 25px;
		margin-top: 25px;
	}
	.additional-grid {
		display: grid;
		grid-template-columns: repeat(2, minmax(0, 1fr));
		gap: 25px;
	}
	@media (max-width: 800px) {
		.about-grid {
			grid-template-columns: 1fr;
			gap: 0;
		}
		.about-copy {
			max-width: 650px;
		}
	}
	@media (max-width: 600px) {
		.project-grid,
		.additional-grid {
			grid-template-columns: 1fr;
			gap: 22px;
		}
		.about-copy p:first-child {
			font-size: 18px;
		}
	}
</style>
