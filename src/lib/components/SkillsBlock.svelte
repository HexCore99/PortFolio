<script lang="ts">
	import { NeoPill } from '@dvcol/neo-svelte/pill';
	import { skills } from '#lib/data/portfolio.js';
	import SkillIcon from './SkillIcon.svelte';
</script>

<div class="skills-tree">
	{#each skills as group (group.title)}
		<div class="skill-row">
			<h3>{group.title}</h3>
			<ul aria-label={group.title}>
				{#each group.items as skill (skill)}
					<li>
						<NeoPill class="tree-chip" elevation={0} rounded={false}
							><SkillIcon name={skill} />{skill}</NeoPill
						>
					</li>
				{/each}
			</ul>
		</div>
	{/each}
</div>

<style>
	.skill-row {
		display: grid;
		grid-template-columns: 170px minmax(0, 1fr);
		gap: 20px;
		padding: 22px 0;
		border-bottom: 1px solid var(--line);
		align-items: start;
	}
	.skill-row:first-child {
		padding-top: 0;
	}
	h3 {
		font-size: 16px;
		line-height: 1.5;
		margin: 8px 0;
		letter-spacing: -0.3px;
	}
	ul {
		display: flex;
		flex-wrap: wrap;
		gap: 10px;
		list-style: none;
		padding: 0;
		margin: 0;
		min-width: 0;
	}
	.skills-tree :global(.tree-chip) {
		display: inline-flex;
		gap: 8px;
		align-items: center;
		padding: 8px 11px;
		border: 1px solid #c5cdd7;
		border-radius: 7px;
		background: #edf0f3;
		color: var(--ink);
		font-size: 13px;
		line-height: 1.5;
		box-shadow: 2px 3px 0 #182a4112;
		max-width: 100%;
	}
	li {
		max-width: 100%;
	}
	@media (max-width: 650px) {
		.skill-row {
			grid-template-columns: 1fr;
			gap: 12px;
		}
		h3 {
			margin: 0;
		}
	}
</style>
