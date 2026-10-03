<script lang="ts">
	import Icon from './Icon.svelte';
	import { profile } from '#lib/data/portfolio.js';
</script>

<section class="hero" aria-labelledby="hero-title">
	<div class="hero-grid container">
		<div class="hero-copy entrance">
			<p class="eyebrow">SOFTWARE DEVELOPER / SIABUL HASSAN</p>
			<h1 id="hero-title" aria-label="Siabul Hassan">
				<span><i>S</i>I<span class="mauve-letter">A</span>BUL</span><span
					>H<span class="cream-letter">A</span>SS<span class="mustard-letter">A</span>N<span
						class="name-dot">.</span
					></span
				>
			</h1>
			<p class="hero-statement">
				Building useful software across<br class="wide-break" /> web, desktop, and systems.
			</p>
			<p class="hero-description">
				From local-first desktop tools to full-stack platforms and C++ experiments. Practical
				problems, built into working software.
			</p>
			<div class="hero-actions">
				<a class="button button-primary" href="#work"
					>See the work <Icon name="arrow" size={19} /></a
				><a class="button button-secondary" href="#contact"
					>Let’s talk <Icon name="arrow" size={19} /></a
				><a class="button button-stone" href="#about">Who I am <Icon name="down" size={17} /></a>
			</div>
		</div>
		<div class="hero-art entrance" aria-hidden="true">
			<svg viewBox="0 0 380 380" class="build-orbit">
				<defs
					><path
						id="orbit-type"
						d="M190,190m-151,0a151,151 0 1,1 302,0a151,151 0 1,1 -302,0"
					/></defs
				>
				<text class="orbit-text"
					><textPath href="#orbit-type" textLength="939"
						>BUILD · LEARN · REFINE · REPEAT · BUILD · LEARN · REFINE · REPEAT ·
					</textPath></text
				>
				<circle
					cx="190"
					cy="190"
					r="126"
					fill="none"
					stroke="currentColor"
					stroke-width="3"
					stroke-dasharray="1 15"
					stroke-linecap="round"
				/>
				<circle cx="190" cy="190" r="95" fill="none" stroke="currentColor" stroke-width="2" />
				{#each Array.from({ length: 12 }, (_, i) => i) as i (i)}<path
						d="M190 112v20"
						stroke="currentColor"
						stroke-width="7"
						transform={'rotate(' + i * 30 + ' 190 190)'}
					/>{/each}
				<rect x="153" y="156" width="82" height="82" rx="3" fill="#111111" />
				<rect
					x="148"
					y="150"
					width="82"
					height="82"
					rx="3"
					fill="#dda51e"
					stroke="#111111"
					stroke-width="3"
				/>
				<text x="189" y="204" text-anchor="middle" class="code-mark">&lt;/&gt;</text>
				<rect
					x="180"
					y="52"
					width="25"
					height="25"
					fill="#b86a8e"
					stroke="#111111"
					stroke-width="3"
				/>
				<rect
					x="273"
					y="259"
					width="18"
					height="18"
					fill="#719267"
					stroke="#111111"
					stroke-width="3"
				/>
				<rect
					x="91"
					y="107"
					width="15"
					height="15"
					fill="#dda51e"
					stroke="#111111"
					stroke-width="3"
				/>
				<circle cx="87" cy="269" r="9" fill="#a4a52b" stroke="#111111" stroke-width="3" />
				<circle cx="71" cy="153" r="6" fill="#b86a8e" stroke="#111111" stroke-width="3" />
				<path
					d="M29 40h10v10H29zM337 312h10v10h-10z"
					fill="#a4a52b"
					stroke="#111111"
					stroke-width="3"
				/>
			</svg>
			<p>WEB / DESKTOP / SYSTEMS</p>
		</div>
		<div class="hero-bottom">
			<span>THOUGHTFUL INTERFACES. SOLID FOUNDATIONS.</span>
			<div>
				<a
					href={profile.github}
					target="_blank"
					rel="noreferrer"
					aria-label="Siabul Hassan on GitHub (opens in a new tab)"
					><Icon name="github" size={16} /> GitHub <Icon name="arrow" size={14} /></a
				><a
					href={profile.linkedin}
					target="_blank"
					rel="noreferrer"
					aria-label="Siabul Hassan on LinkedIn (opens in a new tab)"
					><Icon name="linkedin" size={16} /> LinkedIn <Icon name="arrow" size={14} /></a
				>
			</div>
		</div>
	</div>
</section>

<style>
	.hero {
		background: var(--teal);
		border-bottom: 3px solid var(--ink);
		padding: 76px 0 0;
	}
	.hero-grid {
		display: grid;
		grid-template-columns: 1.3fr 1fr;
		gap: 30px;
	}
	.eyebrow {
		font-size: 11px;
		letter-spacing: 2.4px;
		margin-bottom: 23px;
		color: var(--ink);
		font-weight: 700;
	}
	h1 {
		font-size: clamp(68px, 7.1vw, 96px);
		line-height: 0.96;
		letter-spacing: -5px;
		font-weight: 950;
	}
	h1 > span {
		display: block;
	}
	h1 i {
		font-style: normal;
		color: #493300;
	}
	.mauve-letter {
		color: #55203b;
	}
	.cream-letter {
		color: var(--cream);
	}
	.mustard-letter {
		color: #493300;
	}
	.name-dot {
		color: var(--cream);
	}
	.hero-statement {
		font-size: 23px;
		font-weight: 750;
		line-height: 1.4;
		margin-top: 29px;
		letter-spacing: -0.5px;
		max-width: 550px;
	}
	.hero-description {
		font-size: 14px;
		line-height: 1.8;
		margin-top: 13px;
		max-width: 460px;
		color: #0b2021;
	}
	.hero-actions {
		display: flex;
		flex-wrap: wrap;
		gap: 14px;
		margin-top: 28px;
	}
	.hero-art {
		align-self: center;
		color: #174b4e;
		padding-top: 22px;
	}
	.build-orbit {
		width: 100%;
		max-width: 380px;
		margin: auto;
	}
	.orbit-text {
		font: 700 13px var(--mono);
		letter-spacing: 2px;
		fill: currentColor;
	}
	.code-mark {
		font: 900 29px var(--mono);
		fill: var(--ink);
	}
	.hero-art p {
		text-align: center;
		margin-top: 14px;
		font: 700 10px var(--mono);
		letter-spacing: 2px;
	}
	.hero-bottom {
		grid-column: 1 / -1;
		display: flex;
		align-items: center;
		justify-content: space-between;
		border-top: 1px solid #275d60;
		padding: 18px 0;
		margin-top: 25px;
		gap: 20px;
		font: 10px var(--mono);
		letter-spacing: 0.4px;
	}
	.hero-bottom > div {
		display: flex;
		gap: 23px;
	}
	.hero-bottom a {
		display: flex;
		align-items: center;
		gap: 7px;
		text-decoration: none;
		min-height: 32px;
		font-weight: 700;
	}
	.hero-bottom a:hover {
		text-decoration: underline;
		text-underline-offset: 4px;
	}
	@media (max-width: 1000px) {
		h1 {
			font-size: 78px;
		}
		.hero-grid {
			gap: 20px;
		}
		.hero-art {
			padding-top: 0;
		}
		.hero-statement {
			font-size: 21px;
		}
		.hero-actions {
			gap: 12px;
		}
	}
	@media (max-width: 800px) {
		.hero {
			padding-top: 55px;
		}
		.hero-grid {
			grid-template-columns: 1.5fr 1fr;
			gap: 15px;
		}
		h1 {
			font-size: 66px;
			letter-spacing: -3.5px;
		}
		.hero-art {
			align-self: start;
			margin-top: 65px;
		}
		.hero-statement {
			font-size: 19px;
		}
		.eyebrow {
			font-size: 9px;
			letter-spacing: 1.5px;
		}
		.hero-bottom {
			font-size: 8px;
		}
	}
	@media (max-width: 600px) {
		.hero {
			padding-top: 42px;
		}
		.hero-grid {
			grid-template-columns: 1fr;
		}
		h1 {
			font-size: clamp(58px, 13.5vw, 81px);
			letter-spacing: -3px;
		}
		.hero-art {
			display: none;
		}
		.eyebrow {
			font-size: 9px;
			letter-spacing: 1.5px;
		}
		.hero-statement {
			font-size: 21px;
		}
		.hero-description {
			font-size: 13px;
		}
		.hero-bottom {
			flex-direction: column;
			align-items: flex-start;
			gap: 8px;
			margin-top: 23px;
			font-size: 9px;
		}
		.hero-actions {
			gap: 12px;
		}
	}
</style>
