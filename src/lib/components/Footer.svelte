<script lang="ts">
	import Icon from './Icon.svelte';
	import { profile } from '#lib/data/portfolio.js';
</script>

<footer id="contact">
	<div class="contact-section">
		<div class="contact-panel container">
			<div>
				<p class="eyebrow">04 / GET IN TOUCH</p>
				<h2>LET’S BUILD<br />SOMETHING USEFUL.</h2>
				<p class="contact-copy">Have a role or a project in mind? Let’s talk about it.</p>
			</div>
			<a class="button button-stone email-link" href={'mailto:' + profile.email}
				>{profile.email}<Icon name="arrow" size={21} /></a
			>
		</div>
	</div>
	<div class="footer-bottom container">
		<div>
			<a href="#top" class="footer-brand" aria-label="Siabul Hassan, back to top"
				>SIABUL HASSAN<span>_</span></a
			>
			<p>Software Developer · Built with SvelteKit · © {new Date().getFullYear()}</p>
		</div>
		<div class="footer-links">
			<a class="button github" href={profile.github} target="_blank" rel="noreferrer"
				>GitHub <Icon name="arrow" size={13} /><span class="sr-only"> (opens in a new tab)</span></a
			><a class="button linkedin" href={profile.linkedin} target="_blank" rel="noreferrer"
				>LinkedIn <Icon name="arrow" size={13} /><span class="sr-only">
					(opens in a new tab)</span
				></a
			><a class="button email" href={'mailto:' + profile.email}
				>Email <Icon name="arrow" size={13} /></a
			>
		</div>
	</div>
</footer>

<style>
	footer {
		scroll-margin-top: 80px;
	}
	.contact-section {
		background: var(--mustard);
		border-block: 3px solid var(--ink);
	}
	.contact-panel {
		padding-block: 55px;
		display: flex;
		justify-content: space-between;
		align-items: center;
		gap: 30px;
	}
	.eyebrow {
		color: var(--ink);
		margin-bottom: 19px;
	}
	h2 {
		font-size: clamp(29px, 3.4vw, 43px);
		font-weight: 950;
		line-height: 1.03;
		letter-spacing: -1.8px;
	}
	.contact-copy {
		font-size: 13px;
		margin-top: 20px;
		line-height: 1.8;
	}
	.email-link {
		font: 700 11px var(--mono);
		text-transform: none;
		gap: 16px;
		white-space: nowrap;
	}
	.footer-bottom {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 25px;
		padding-block: 33px;
	}
	.footer-brand {
		font-size: 20px;
		font-weight: 950;
		letter-spacing: -0.7px;
		text-decoration: none;
	}
	.footer-brand span {
		color: #a33632;
	}
	.footer-bottom p {
		font: 10px var(--mono);
		color: var(--muted);
		margin-top: 10px;
		line-height: 1.8;
	}
	.footer-links {
		display: flex;
		gap: 11px;
	}
	.footer-links a {
		font: 700 10px var(--mono);
		padding: 10px 12px;
		gap: 9px;
		min-height: 40px;
	}
	.github {
		background: var(--olive);
	}
	.linkedin {
		background: var(--teal);
	}
	.email {
		background: var(--mustard);
	}
	@media (max-width: 800px) {
		.contact-panel {
			flex-direction: column;
			align-items: flex-start;
			gap: 26px;
		}
		.footer-bottom {
			flex-direction: column;
			align-items: flex-start;
		}
	}
	@media (max-width: 500px) {
		.contact-panel {
			padding-block: 40px;
		}
		.email-link {
			font-size: 10px;
			padding-inline: 13px;
		}
	}
</style>
