<script lang="ts">
	import { skills } from '#lib/data/portfolio.js';
	import SkillIcon from './SkillIcon.svelte';
</script>

<div class="skills-tree">
	{#each skills as group (group.title)}
		<div class="skill-row">
			<h3>{group.title}</h3>
			<ul aria-label={group.title}>
				{#each group.items as skill (skill)}
					<li class="tree-chip"><SkillIcon name={skill} />{skill}</li>
				{/each}
			</ul>
		</div>
	{/each}
</div>

<style>
	.skill-row {
		--skill-background: #f1ccab;
		--skill-ink: #704528;
		display: grid;
		grid-template-columns: 170px minmax(0, 1fr);
		gap: 20px;
		padding: 26px 0;
		border-bottom: 1px solid var(--line);
		align-items: start;
	}
	.skill-row:first-child {
		padding-top: 0;
	}
	.skill-row:nth-child(2) {
		--skill-background: #c8dfc9;
		--skill-ink: #315b47;
	}
	.skill-row:nth-child(3) {
		--skill-background: #cbdcf1;
		--skill-ink: #385579;
	}
	.skill-row:nth-child(4) {
		--skill-background: #ddc9ea;
		--skill-ink: #69467d;
	}
	.skill-row:nth-child(5) {
		--skill-background: #efdda1;
		--skill-ink: #675524;
	}
	h3 {
		color: var(--skill-ink);
		font-size: 16px;
		line-height: 1.5;
		margin: 8px 0;
		letter-spacing: -0.3px;
	}
	ul {
		display: flex;
		flex-wrap: wrap;
		gap: 14px;
		list-style: none;
		padding: 0 4px 4px 0;
		margin: 0;
		min-width: 0;
	}
	.tree-chip {
		display: inline-flex;
		gap: 9px;
		align-items: center;
		padding: 9px 12px;
		border: 1.5px solid var(--ink);
		border-radius: 3px;
		box-shadow: 3px 3px 0 var(--ink);
		background: var(--skill-background);
		color: var(--ink);
		font: 600 12px/1.5 var(--mono);
		overflow-wrap: anywhere;
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
