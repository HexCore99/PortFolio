<script lang="ts">
	import Navigation from '#lib/components/Navigation.svelte';
	import Hero from '#lib/components/Hero.svelte';
	import SectionHeading from '#lib/components/SectionHeading.svelte';
	import SkillsBlock from '#lib/components/SkillsBlock.svelte';
	import EducationBlock from '#lib/components/EducationBlock.svelte';
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
	<section id="work" class="work-section section" aria-labelledby="work-title">
		<div class="container work-layout">
			<div class="section-rail"><SectionHeading id="work-title" title="Selected work" /></div>
			<div class="work-content">
				{#each projects.filter((project) => project.featured) as project (project.id)}<ProjectCard
						{project}
					/>{/each}
				<div class="project-grid">
					{#each projects.filter((project) => !project.featured && !project.additional) as project (project.id)}<ProjectCard
							{project}
						/>{/each}
				</div>
			</div>
		</div>
	</section>
	<section
		class="section additional-section container work-layout"
		aria-labelledby="additional-title"
	>
		<div class="section-rail">
			<SectionHeading id="additional-title" title="Additional builds" />
		</div>
		<div class="additional-grid">
			{#each projects.filter((project) => project.additional) as project (project.id)}<ProjectCard
					{project}
					compact
				/>{/each}
		</div>
	</section>
	<section id="about" class="section container work-layout" aria-labelledby="about-title">
		<div class="section-rail"><SectionHeading id="about-title" title="Skills" /></div>
		<div class="skills-content"><SkillsBlock /></div>
	</section>
	<section
		class="section container work-layout education-section"
		aria-labelledby="education-title"
	>
		<div class="section-rail"><SectionHeading id="education-title" title="Education" /></div>
		<EducationBlock />
	</section>
</main>
<Footer />

<style>
	.education-section,
	#about {
		padding-top: 0;
	}
	.skills-content {
		min-width: 0;
	}
	.work-layout {
		display: grid;
		grid-template-columns: 200px minmax(0, 1fr);
		gap: 40px;
		align-items: start;
	}
	.work-content,
	.additional-grid {
		min-width: 0;
	}
	.section-rail {
		position: sticky;
		top: 120px;
		align-self: start;
	}
	.section-rail :global(.section-heading) {
		margin: 0;
	}
	.section-rail :global(h2) {
		max-width: 180px;
		font-size: 34px;
		line-height: 1.12;
		letter-spacing: -1.3px;
	}
	@media (max-width: 1100px) {
		.work-layout {
			grid-template-columns: 150px minmax(0, 1fr);
			gap: 28px;
		}
		.section-rail :global(h2) {
			font-size: 29px;
			max-width: 150px;
		}
	}
	@media (max-width: 1100px) {
		.work-layout {
			grid-template-columns: 1fr;
			gap: 30px;
		}
		.section-rail {
			position: static;
		}
		.section-rail :global(h2) {
			max-width: none;
			font-size: 36px;
		}
	}
	@media (max-width: 600px) {
		.section-rail :global(h2) {
			font-size: 32px;
		}
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
	@media (max-width: 740px) {
		.project-grid,
		.additional-grid {
			grid-template-columns: 1fr;
			gap: 22px;
		}
	}
</style>
