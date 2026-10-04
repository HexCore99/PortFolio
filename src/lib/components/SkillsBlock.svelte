<script lang="ts">
	import { NeoPill } from '@dvcol/neo-svelte/pill';
	import { skills } from '#lib/data/portfolio.js';
</script>

<div class="skills-grid">
	{#each skills as skill (skill.title)}
		<div class="skill-block">
			<h3>{skill.title}</h3>
			<ul>
				{#each skill.items as item (item)}<li>
						<NeoPill class="skill-chip" elevation={0} rounded={false}>{item}</NeoPill>
					</li>{/each}
			</ul>
		</div>
	{/each}
</div>

<style>
	.skills-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		border-top: 1px solid var(--line);
		margin-top: 40px;
		padding-top: 28px;
		gap: 32px;
	}
	h3 {
		font-size: 16px;
		font-weight: 700;
		text-transform: none;
		margin: 10px 0 15px;
		letter-spacing: -0.3px;
	}
	ul {
		display: flex;
		gap: 10px;
		flex-wrap: wrap;
		list-style: none;
		padding: 0;
		color: var(--muted);
		font: 12px var(--mono);
		line-height: 1.8;
	}
	@media (max-width: 600px) {
		.skills-grid {
			grid-template-columns: 1fr;
			gap: 25px;
		}
		.skill-block {
			position: relative;
			padding-left: 0;
		}
	}
</style>
