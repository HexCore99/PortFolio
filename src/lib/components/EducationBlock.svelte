<script lang="ts">
	import { education } from '#lib/data/portfolio.js';
	import { NeoPill } from '@dvcol/neo-svelte/pill';
</script>

<div class="education-details">
	<h3>{education.degree}</h3>
	<p class="institution">{education.institution}</p>
	<div class="study-meta">
		<span>{education.dates}</span>
		<NeoPill class="trimester" elevation={0} rounded={false}>{education.trimester}</NeoPill>
	</div>
	<p class="description">{education.description}</p>
	<div class="coursework">
		<h4>Relevant coursework</h4>
		<ul>
			{#each education.coursework as course (course)}
				<li><NeoPill class="course-chip" elevation={0} rounded={false}>{course}</NeoPill></li>
			{/each}
		</ul>
	</div>
	<div class="scholarship">
		<h4>Scholarship</h4>
		<p>{education.scholarship}</p>
	</div>
</div>

<style>
	.education-details {
		min-width: 0;
		border-top: 1px solid var(--line);
		padding-top: 26px;
	}
	h3 {
		font-size: clamp(23px, 2.3vw, 30px);
		line-height: 1.3;
		letter-spacing: -0.7px;
		font-weight: 700;
	}
	.institution {
		font-size: 17px;
		margin-top: 10px;
		line-height: 1.6;
	}
	.study-meta {
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		gap: 15px 24px;
		margin-top: 24px;
		color: var(--muted);
		font-size: 14px;
	}
	.study-meta :global(.trimester) {
		padding: 7px 12px;
		border: 1px solid #d5b8a3;
		border-radius: 6px;
		background: #fae3d5;
		color: #623e2c;
		font-size: 13px;
	}
	.description {
		max-width: 590px;
		margin-top: 26px;
		font-size: 16px;
		line-height: 1.8;
		color: var(--muted);
	}
	h4 {
		margin: 0 0 14px;
		font-size: 12px;
		text-transform: uppercase;
		letter-spacing: 1px;
		font-weight: 650;
	}
	.coursework {
		margin-top: 32px;
	}
	ul {
		display: flex;
		flex-wrap: wrap;
		gap: 10px;
		list-style: none;
		margin: 0;
		padding: 0;
	}
	li {
		max-width: 100%;
	}
	.coursework :global(.course-chip) {
		padding: 9px 13px;
		border: 1px solid #c4ccd7;
		border-radius: 6px;
		background: #edf0f3;
		font-size: 13px;
		line-height: 1.5;
		box-shadow: 2px 3px 0 #182a4112;
		max-width: 100%;
	}
	.scholarship {
		margin-top: 32px;
		padding-top: 24px;
		border-top: 1px solid var(--line);
	}
	.scholarship p {
		font-size: 15px;
		line-height: 1.8;
		color: var(--muted);
		max-width: 590px;
	}
	@media (max-width: 600px) {
		.education-details {
			padding-top: 22px;
		}
		.institution {
			font-size: 16px;
		}
		.description {
			font-size: 15px;
		}
		.study-meta {
			gap: 12px;
		}
	}
</style>
