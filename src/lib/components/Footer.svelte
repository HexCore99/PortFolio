<script lang="ts">
	import { NeoButton } from '@dvcol/neo-svelte/buttons';
	import Icon from './Icon.svelte';
	import ResumeLink from './ResumeLink.svelte';
	import { profile } from '#lib/data/portfolio.js';
</script>

<footer id="contact">
	<div class="contact-section container">
		<div class="contact-main">
			<h2>Have something<br />in <span>mind?</span></h2>
			<div class="contact-copy">
				<p>A role, a project, or a technical conversation.<br />I’d be happy to hear from you.</p>
				<a class="email-address" href={'mailto:' + profile.email}
					>{profile.email}<Icon name="arrow" size={20} /></a
				>
			</div>
		</div>
		<div class="contact-bottom">
			<div class="contact-links">
				<NeoButton
					elevation={0}
					hover={0}
					active={0}
					scale={false}
					class="button button-primary"
					href={'mailto:' + profile.email}
					><Icon name="mail" size={19} /> Say hello <Icon name="arrow" size={18} /></NeoButton
				><NeoButton
					elevation={0}
					hover={0}
					active={0}
					scale={false}
					class="button button-secondary"
					href={profile.github}
					{...{ target: '_blank', rel: 'noreferrer' }}
					><Icon name="github" size={18} /> GitHub <Icon name="arrow" size={17} /><span
						class="sr-only"
					>
						(opens in a new tab)</span
					></NeoButton
				><NeoButton
					elevation={0}
					hover={0}
					active={0}
					scale={false}
					class="button button-secondary"
					href={profile.linkedin}
					{...{ target: '_blank', rel: 'noreferrer' }}
					><Icon name="linkedin" size={18} /> LinkedIn <Icon name="arrow" size={17} /><span
						class="sr-only"
					>
						(opens in a new tab)</span
					></NeoButton
				>
			</div>
			<ResumeLink />
		</div>
	</div>
	<div class="footer-band">
		<div class="footer-signature container">
			<a class="footer-identity" href="#top" aria-label="Siabul Hassan, back to top">
				<span class="footer-mark" aria-hidden="true">sh.</span>
				<span class="identity-copy">
					<strong>Siabul Hassan</strong>
					<small>Building useful software.</small>
				</span>
			</a>
			<div class="footer-meta">
				<span class="signature-copyright">© {new Date().getFullYear()}</span>
				<a class="back-to-top" href="#top"><span aria-hidden="true">↑</span> Back to top</a>
			</div>
		</div>
	</div>
</footer>

<style>
	.footer-band {
		margin-top: 44px;
		background: var(--surface-muted);
		border-top: 1px solid var(--line);
	}
	footer {
		scroll-margin-top: 15px;
		padding-top: 15px;
	}
	.contact-section {
		background: var(--contact-background);
		color: var(--ink);
		border: 1.5px solid var(--ink);
		border-radius: 12px;
		padding: 36px 44px;
	}
	.contact-section a:focus-visible {
		outline-color: var(--blue);
	}
	.contact-main {
		display: grid;
		grid-template-columns: 1fr 1fr;
		align-items: end;
		gap: 35px;
		padding: 26px 0 37px;
	}
	h2 {
		font-size: clamp(40px, 5.2vw, 66px);
		font-weight: 650;
		line-height: 1.04;
		letter-spacing: -3px;
	}
	h2 span {
		color: var(--blue);
	}
	.contact-copy p {
		font-size: 15px;
		line-height: 1.8;
		color: var(--contact-muted);
	}
	.email-address {
		display: inline-flex;
		align-items: center;
		gap: 25px;
		margin-top: 20px;
		font-size: 16px;
		text-decoration: none;
		padding-bottom: 7px;
		border-bottom: 1px solid #a88f7e;
	}
	.email-address:hover {
		color: var(--blue);
	}
	.contact-bottom {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 20px;
		border-top: 1px solid #bca18f;
		padding-top: 27px;
	}
	.contact-links {
		--button-shadow: 0 3px 0 #182a41;
		display: flex;
		gap: 15px;
		flex-wrap: wrap;
	}
	.contact-links :global(.button) {
		border-color: #0d1827;
		box-shadow: 0 4px 0 #0d1827;
		gap: 12px;
	}
	@media (max-width: 850px) {
		.contact-section {
			padding: 30px;
		}
		.contact-main {
			grid-template-columns: 1fr;
			gap: 25px;
		}
		.contact-bottom {
			flex-direction: column;
			align-items: flex-start;
			gap: 24px;
		}
	}
	@media (max-width: 600px) {
		.contact-section {
			padding: 25px 21px;
		}
		h2 {
			font-size: clamp(34px, 11vw, 47px);
			letter-spacing: -2px;
		}
		.contact-copy p {
			font-size: 13px;
		}
		.email-address {
			font-size: 13px;
			gap: 10px;
		}
		.contact-links {
			width: 100%;
			gap: 13px;
		}
		.contact-links :global(.button) {
			flex: 1 1 140px;
			font-size: 12px;
			padding-inline: 13px;
			gap: 10px;
		}
	}

	.footer-signature {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 32px;
		padding-block: 25px;
	}
	.footer-identity {
		display: inline-flex;
		align-items: center;
		gap: 13px;
		color: var(--ink);
		text-decoration: none;
	}
	.footer-mark {
		display: grid;
		place-items: center;
		width: 40px;
		height: 40px;
		padding-bottom: 3px;
		border: 1.5px solid var(--ink);
		border-radius: 11px 4px 11px 4px;
		background: var(--brand-background);
		color: var(--on-bright);
		box-shadow: 2px 2px 0 var(--ink);
		font-size: 21px;
		font-weight: 850;
		letter-spacing: -1.5px;
	}
	.identity-copy {
		display: grid;
		gap: 3px;
	}
	.identity-copy strong {
		font-size: 15px;
		letter-spacing: -0.2px;
	}
	.identity-copy small {
		color: var(--muted);
		font-size: 11px;
	}
	.footer-meta {
		display: flex;
		align-items: center;
		gap: 24px;
	}
	.signature-copyright {
		font-size: 12px;
		color: var(--muted);
		white-space: nowrap;
	}
	.back-to-top {
		display: inline-flex;
		align-items: center;
		gap: 8px;
		min-height: 40px;
		padding: 9px 12px;
		border: 1px solid var(--line-strong);
		border-radius: 4px;
		background: var(--paper);
		box-shadow: 2px 2px 0 var(--ink);
		font-size: 12px;
		font-weight: 650;
		text-decoration: none;
		transition:
			transform 0.15s,
			box-shadow 0.15s;
	}
	.back-to-top:hover {
		transform: translate(1px, 1px);
		box-shadow: 1px 1px 0 var(--ink);
	}
	.back-to-top span {
		color: var(--blue);
		font-size: 16px;
	}
	@media (max-width: 520px) {
		.footer-signature {
			align-items: flex-start;
			flex-direction: column;
			gap: 20px;
		}
		.footer-meta {
			width: 100%;
			justify-content: space-between;
		}
		.signature-copyright {
			font-size: 11px;
		}
	}
	@media (prefers-reduced-motion: reduce) {
		.back-to-top:hover {
			transform: none;
		}
	}
</style>
