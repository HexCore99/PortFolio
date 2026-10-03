<script lang="ts">
	import { skills } from '#lib/data/portfolio.js';
</script>

<div class="skills-grid">
	{#each skills as skill (skill.title)}
		<div class="skill-block">
			<span class="skill-number">{skill.number}</span>
			<h3>{skill.title}</h3>
			<ul>
				{#each skill.items as item (item)}<li>{item}</li>{/each}
			</ul>
		</div>
	{/each}
</div>

<style>
	.skills-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		border-top: 2px solid var(--line);
		margin-top: 40px;
		padding-top: 28px;
		gap: 32px;
	}
	.skill-number {
		font: 11px var(--mono);
		color: var(--muted);
	}
	h3 {
		font-size: 16px;
		font-weight: 850;
		text-transform: uppercase;
		margin: 10px 0 15px;
		letter-spacing: -0.3px;
	}
	ul {
		display: flex;
		gap: 7px 16px;
		flex-wrap: wrap;
		list-style: none;
		padding: 0;
		color: var(--muted);
		font: 11px var(--mono);
		line-height: 1.8;
	}
	@media (max-width: 600px) {
		.skills-grid {
			grid-template-columns: 1fr;
			gap: 25px;
		}
		.skill-block {
			position: relative;
			padding-left: 34px;
		}
		.skill-number {
			position: absolute;
			left: 0;
			top: 14px;
		}
	}
</style>
