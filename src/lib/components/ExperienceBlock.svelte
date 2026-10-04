<script lang="ts">
	import { experience } from '#lib/data/portfolio.js';
</script>

<div class="experience-details">
	<h3>{experience.role}</h3>
	<p class="institution">{experience.institution}</p>
	<p class="department">{experience.department}</p>

	<div class="course-block">
		<h4>Course focus</h4>
		<h5>{experience.course}</h5>
		<p>{experience.description}</p>
	</div>

	<ul class="responsibilities">
		{#each experience.responsibilities as responsibility (responsibility)}
			<li>{responsibility}</li>
		{/each}
	</ul>

	<ul class="tags" aria-label="Experience skills">
		{#each experience.tags as tag (tag)}
			<li>{tag}</li>
		{/each}
	</ul>
</div>

<style>
	.experience-details {
		min-width: 0;
		padding-top: 26px;
		border-top: 1px solid var(--line);
	}
	h3 {
		font-size: clamp(23px, 2.3vw, 30px);
		line-height: 1.3;
		letter-spacing: -0.7px;
		font-weight: 700;
	}
	.institution {
		margin-top: 10px;
		font-size: 17px;
		line-height: 1.6;
	}
	.department {
		margin-top: 2px;
		color: var(--muted);
		font-size: 14px;
		line-height: 1.6;
	}
	.course-block {
		max-width: 760px;
		margin-top: 28px;
		padding-top: 24px;
		border-top: 1px solid var(--line);
	}
	h4 {
		margin: 0 0 14px;
		font-size: 12px;
		font-weight: 650;
		letter-spacing: 1px;
		text-transform: uppercase;
	}
	h5 {
		margin: 0;
		font-size: 19px;
		line-height: 1.4;
		letter-spacing: -0.3px;
	}
	.course-block > p:last-child {
		margin-top: 14px;
		color: var(--muted);
		font-size: 16px;
		line-height: 1.8;
	}
	.responsibilities {
		display: grid;
		gap: 9px;
		max-width: 760px;
		margin: 24px 0 0;
		padding: 0;
		list-style: none;
	}
	.responsibilities li {
		position: relative;
		padding-left: 22px;
		font-size: 15px;
		line-height: 1.65;
	}
	.responsibilities li::before {
		content: '•';
		position: absolute;
		left: 3px;
		color: var(--blue);
		font-size: 20px;
		line-height: 1.1;
	}
	.tags {
		display: flex;
		flex-wrap: wrap;
		gap: 10px;
		margin: 26px 0 0;
		padding: 0;
		list-style: none;
	}
	.tags li {
		max-width: 100%;
		padding: 9px 13px;
		border: 0;
		border-radius: 3px;
		background: var(--chip-neutral);
		color: var(--muted);
		font-size: 13px;
		line-height: 1.5;
	}
	@media (max-width: 600px) {
		.experience-details {
			padding-top: 22px;
		}
		.institution {
			font-size: 16px;
		}
		.course-block > p:last-child,
		.responsibilities li {
			font-size: 15px;
		}
	}
</style>
