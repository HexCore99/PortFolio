<script lang="ts">
	import { asset } from '$app/paths';
	import Icon from './Icon.svelte';
</script>

<a
	class="resume-link"
	href={asset('resume/Siabul-Hassan-Resume.pdf')}
	download="Siabul-Hassan-Resume.pdf"
>
	<Icon name="down" size={17} />
	<span>Download résumé</span>
	<span class="file-type">PDF</span>
</a>

<style>
	.resume-link {
		display: inline-flex;
		align-items: center;
		gap: 12px;
		min-height: 52px;
		padding: 12px 17px;
		border: 2px solid var(--ink);
		border-radius: 6px;
		background: #f4ce67;
		box-shadow: 4px 4px 0 var(--ink);
		transition:
			transform 0.15s ease,
			box-shadow 0.15s ease,
			background 0.15s ease;
		width: fit-content;
		color: var(--ink);
		font: 700 13px/1.4 var(--mono);
		text-decoration: none;
	}
	.resume-link:hover {
		background: #ffdb79;
		transform: translate(-1px, -1px);
		box-shadow: 5px 5px 0 var(--ink);
	}
	.resume-link:active {
		transform: translate(3px, 3px);
		box-shadow: 1px 1px 0 var(--ink);
	}
	.file-type {
		color: var(--ink);
		border-left: 1px solid #182a4140;
		padding-left: 10px;
		font: 11px var(--mono);
		font-weight: 400;
	}
	@media (prefers-reduced-motion: reduce) {
		.resume-link:hover,
		.resume-link:active {
			transform: none;
		}
	}
</style>
