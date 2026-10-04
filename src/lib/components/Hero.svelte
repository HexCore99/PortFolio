<script lang="ts">
	import { NeoButton } from '@dvcol/neo-svelte/buttons';
	import Icon from './Icon.svelte';
	import BuildBench from './BuildBench.svelte';
	import { profile } from '#lib/data/portfolio.js';
</script>

<section class="hero" aria-labelledby="hero-title">
	<div class="hero-grid container">
		<div class="hero-copy entrance">
			<h1 id="hero-title">Building<br />useful software<span class="full-stop">.</span></h1>
			<p class="hero-statement">
				Across <span>web</span>, <span>desktop</span>, and <span>systems</span>.
			</p>
			<p class="hero-description">
				Local-first tools. Full-stack platforms. C++ experiments.<br class="desktop-break" /> I build
				practical solutions—and the pieces that make them work.
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
		</div>
		<BuildBench />
	</div>
	<div class="hero-bottom container">
		<div class="social-links">
			<a
				href={profile.github}
				target="_blank"
				rel="noreferrer"
				aria-label="Siabul Hassan on GitHub (opens in a new tab)"
				><Icon name="github" size={18} /> GitHub <Icon name="arrow" size={14} /></a
			><a
				href={profile.linkedin}
				target="_blank"
				rel="noreferrer"
				aria-label="Siabul Hassan on LinkedIn (opens in a new tab)"
				><Icon name="linkedin" size={18} /> LinkedIn <Icon name="arrow" size={14} /></a
			>
		</div>
	</div>
</section>

<style>
	.hero {
		padding-top: 83px;
	}
	.hero-grid {
		display: grid;
		grid-template-columns: 1.2fr 1fr;
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
		font-size: 15px;
		line-height: 1.85;
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
	.hero-bottom {
		display: flex;
		align-items: center;
		justify-content: flex-end;
		gap: 20px;
		border-block: 1px solid var(--line);
		padding-block: 20px;
		margin-top: 65px;
	}
	.social-links {
		display: flex;
		gap: 23px;
	}
	.social-links a {
		display: inline-flex;
		align-items: center;
		gap: 8px;
		font-size: 12px;
		font-weight: 600;
		text-decoration: none;
		min-height: 34px;
	}
	.hero-bottom a:hover {
		color: var(--blue);
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
		.desktop-break {
			display: none;
		}
	}
	@media (max-width: 850px) {
		.hero {
			padding-top: 60px;
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
		.hero-bottom {
			margin-top: 42px;
		}
	}
	@media (max-width: 600px) {
		.hero {
			padding-top: 43px;
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
		.hero-bottom {
			align-items: flex-start;
			flex-direction: column;
			gap: 16px;
		}
	}
</style>
