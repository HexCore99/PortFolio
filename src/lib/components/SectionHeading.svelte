<script lang="ts">
	let {
		id,
		number,
		title,
		description
	}: { id: string; number: string; title: string; description?: string } = $props();
</script>

<div class="section-heading">
	<div>
		<p class="eyebrow"><span>{number}</span> / {title}</p>
		<h2 {id}>{title}<span class="accent">.</span></h2>
	</div>
	{#if description}<p class="section-description">{description}</p>{/if}
</div>

<style>
	.section-heading {
		display: flex;
		justify-content: space-between;
		align-items: end;
		gap: 32px;
		margin-bottom: 38px;
	}
	.eyebrow {
		margin-bottom: 14px;
	}
	.eyebrow span {
		color: var(--blue);
	}
	h2 {
		font-size: clamp(32px, 4vw, 46px);
		letter-spacing: -1.6px;
		font-weight: 950;
		text-transform: uppercase;
		line-height: 1.15;
	}
	.section-description {
		max-width: 345px;
		font-size: 13px;
		line-height: 1.8;
		color: var(--muted);
		margin-bottom: 3px;
	}
	@media (max-width: 600px) {
		.section-heading {
			align-items: start;
			flex-direction: column;
			gap: 16px;
			margin-bottom: 28px;
		}
	}
</style>
