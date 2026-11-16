<script lang="ts">
	import { asset } from '$app/paths';
	import Icon from './Icon.svelte';

	const resumeUrl = asset('resume/Siabul-Hassan-Resume.pdf');
	let viewing = $state(false);
</script>

<div class="resume-actions" role="group" aria-label="Résumé">
	<span class="paper" aria-hidden="true">
		<span class="paper-heading"></span>
		<span class="paper-line"></span>
		<span class="paper-line"></span>
	</span>
	<div>
		<strong>Résumé</strong>
		<div class="actions">
			<button type="button" aria-haspopup="dialog" onclick={() => (viewing = true)}>View</button>
			<a href={resumeUrl} download="Siabul-Hassan-Resume.pdf"
				><Icon name="down" size={13} /> Download</a
			>
		</div>
	</div>
</div>
{#if viewing}
	<dialog
		aria-label="Résumé viewer"
		{@attach (dialog) => dialog.showModal()}
		onclose={() => (viewing = false)}
	>
		<header>
			<h2>Résumé</h2>
			<form method="dialog"><button class="button button-secondary">Close</button></form>
		</header>
		<div class="preview">
			<img
				src={asset('resume/Siabul-Hassan-Resume.png')}
				width="1556"
				height="2200"
				alt="Siabul Hassan’s one-page software developer résumé"
			/>
		</div>
	</dialog>
{/if}

<style>
	.resume-actions {
		display: flex;
		align-items: center;
		gap: 16px;
		width: fit-content;
		padding: 8px 0;
		color: var(--ink);
	}
	.paper {
		display: grid;
		align-content: center;
		gap: 4px;
		width: 37px;
		height: 46px;
		padding: 7px;
		border: 1.5px solid #36465d;
		border-radius: 3px;
		background: #fffdf7;
		box-shadow: -3px 3px 0 var(--coral);
		transform: rotate(-6deg);
	}
	.paper-heading {
		width: 60%;
		height: 4px;
		background: #354967;
	}
	.paper-line {
		height: 2px;
		background: #a3acb8;
	}
	.paper-line:last-child {
		width: 75%;
	}
	.resume-actions strong {
		display: block;
		font:
			bold 27px/1.05 Georgia,
			serif;
		letter-spacing: -1px;
	}
	.actions {
		display: flex;
		align-items: center;
		gap: 16px;
	}
	.actions a,
	.actions button {
		display: inline-flex;
		align-items: center;
		gap: 4px;
		min-height: 32px;
		padding: 0;
		background: transparent;
		border: 0;
		color: var(--muted);
		font: 600 13px/1.3 var(--mono);
		text-decoration: underline;
		text-decoration-color: var(--line-strong);
		text-underline-offset: 4px;
		cursor: pointer;
	}
	.actions :is(a, button):is(:hover, :focus-visible) {
		color: var(--blue);
	}
	.button {
		font: inherit;
		gap: 7px;
		padding: 10px 16px;
		border-radius: 6px;
		cursor: pointer;
	}
	.button-secondary {
		color: var(--ink);
	}
	dialog {
		width: min(900px, 94vw);
		height: min(960px, 90dvh);
		margin: auto;
		padding: 0;
		border: 2px solid var(--ink);
		border-radius: 10px;
		background: var(--white);
		color: var(--ink);
	}
	dialog[open] {
		display: flex;
		flex-direction: column;
	}
	dialog::backdrop {
		background: rgb(12 23 40 / 70%);
	}
	header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 12px 18px;
		border-bottom: 1px solid var(--ink);
	}
	h2 {
		font-size: 20px;
	}
	form {
		font: 700 13px var(--mono);
	}
	.preview {
		flex: 1;
		min-height: 0;
		overflow: auto;
		overscroll-behavior: contain;
		background: white;
	}
	.preview img {
		display: block;
		width: 100%;
		height: auto;
	}
</style>
