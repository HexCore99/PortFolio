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
			<span class="signature-name">Siabul Hassan<span aria-hidden="true">.</span></span><span
				class="signature-copyright">© {new Date().getFullYear()}</span
			>
		</div>
	</div>
</footer>

<style>
	.footer-band {
		margin-top: 44px;
		background: #284c4a;
		border-top: 4px solid #e9b58d;
	}
	footer {
		scroll-margin-top: 15px;
		padding-top: 15px;
	}
	.contact-section {
		background: #f4d5bf;
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
		color: #455266;
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
		gap: 20px;
		padding-block: 30px;
	}
	.signature-name {
		font-size: clamp(23px, 3vw, 36px);
		font-weight: 750;
		letter-spacing: -0.035em;
		line-height: 1.1;
		color: #f6f3ea;
	}
	.signature-name > span {
		color: #efb58c;
	}
	.signature-copyright {
		font-size: 13px;
		color: #d0dedb;
		white-space: nowrap;
	}
	@media (max-width: 400px) {
		.footer-signature {
			gap: 10px;
		}
		.signature-copyright {
			font-size: 11px;
		}
	}
</style>
