<script lang="ts">
	import { NeoButton } from '@dvcol/neo-svelte/buttons';
	import Icon from './Icon.svelte';
	import BuildBench from './BuildBench.svelte';
	import ResumeLink from './ResumeLink.svelte';
</script>

<section class="hero" aria-labelledby="hero-title">
	<div class="hero-grid container">
		<div class="hero-copy entrance">
			<h1 id="hero-title">Building<br />useful software<span class="full-stop">.</span></h1>
			<p class="hero-statement">
				Across <span>web</span>, <span>desktop</span>, and <span>systems</span>.
			</p>
			<p class="hero-description">
				I'm Siabul Hassan, a CS student at United International University. I like to make desktop
				apps, full-stack platforms and the odd C++ experiment, then ship them with release builds.
			</p>
			<div class="hero-actions">
				<NeoButton
					elevation={0}
					hover={0}
					active={0}
					scale={false}
					class="button button-primary"
					href="#work"
					>Explore my work <span class="button-arrow"><Icon name="arrow" size={21} /></span
					></NeoButton
				>
				<NeoButton
					elevation={0}
					hover={0}
					active={0}
					scale={false}
					class="button button-secondary"
					href="#contact">Get in touch <Icon name="mail" size={19} /></NeoButton
				>
			</div>
			<div class="hero-resume"><ResumeLink /></div>
		</div>
		<BuildBench />
	</div>
</section>

<style>
	.hero-resume {
		margin-top: 14px;
	}
	.hero {
		padding-block: 83px 65px;
	}
	.hero-grid {
		display: grid;
		grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr);
		align-items: center;
		gap: 52px;
	}
	h1 {
		font-size: clamp(52px, 5.5vw, 77px);
		line-height: 1.02;
		letter-spacing: -4.7px;
		font-weight: 800;
	}
	.full-stop {
		color: var(--blue);
	}
	.hero-statement {
		font-size: clamp(20px, 2vw, 26px);
		line-height: 1.5;
		margin-top: 23px;
		font-weight: 500;
		letter-spacing: -0.8px;
	}
	.hero-statement span {
		text-decoration: underline;
		text-decoration-color: var(--coral);
		text-decoration-thickness: 4px;
		text-underline-offset: 6px;
	}
	.hero-description {
		color: var(--muted);
		font-size: 16px;
		line-height: 1.8;
		margin-top: 25px;
		max-width: 485px;
	}
	.hero-actions {
		display: flex;
		flex-wrap: wrap;
		gap: 16px;
		margin-top: 32px;
	}
	.button-arrow {
		border-left: 1px solid #182a4150;
		padding-left: 16px;
	}
	@media (max-width: 1050px) {
		.hero-grid {
			gap: 30px;
		}
		h1 {
			font-size: 62px;
			letter-spacing: -3.8px;
		}
		.hero-actions :global(.button) {
			padding-inline: 16px;
			font-size: 13px;
			gap: 13px;
		}
	}
	@media (max-width: 850px) {
		.hero {
			padding-block: 60px 48px;
		}
		.hero-grid {
			grid-template-columns: 1fr;
			gap: 40px;
		}
		.hero-copy {
			max-width: 620px;
		}
		h1 {
			font-size: 76px;
		}
		.hero-description {
			max-width: 540px;
		}
	}
	@media (max-width: 600px) {
		.hero {
			padding-block: 43px 40px;
		}
		h1 {
			font-size: clamp(44px, 10.8vw, 66px);
			letter-spacing: -2.5px;
		}
		.hero-statement {
			font-size: 20px;
			letter-spacing: -0.6px;
			margin-top: 20px;
		}
		.hero-description {
			font-size: 14px;
			margin-top: 23px;
		}
		.hero-actions {
			gap: 14px;
			margin-top: 27px;
		}
		.hero-actions :global(.button) {
			flex: 1 1 auto;
		}
	}
</style>
