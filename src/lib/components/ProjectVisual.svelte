<script lang="ts">
	import type { Project } from '#lib/data/portfolio.js';
	import { asset } from '$app/paths';
	let { project, compact = false }: { project: Project; compact?: boolean } = $props();
</script>

<div
	class="project-visual"
	class:featured={project.featured}
	class:compact
	class:dark={project.id === 'movies' || project.additional}
>
	{#if project.image}
		<img
			src={asset(project.image.src)}
			alt={project.image.alt}
			width={project.image.width}
			height={project.image.height}
			loading="lazy"
			decoding="async"
		/>
	{:else if project.visual === 'judge'}
		<div
			class="technical judge"
			role="img"
			aria-label="QuickJudge workflow illustration: source code is submitted, evaluated, and returns a verdict."
		>
			<div class="visual-label">
				<span class="tiny-square"></span> THE SUBMISSION PIPELINE <span>01 → 03</span>
			</div>
			<div class="judge-flow">
				<div class="code-symbol">&lt;/&gt;<span>Source code</span></div>
				<span class="connector">→</span>
				<div class="judge-node"><span class="brackets">{'{ }'}</span><span>Evaluate</span></div>
				<span class="connector">→</span>
				<div class="verdict"><span>✓</span><span>Verdict</span></div>
			</div>
			<div class="visual-bottom"><span>PROBLEM → SOLUTION</span><span>QuickJudge</span></div>
		</div>
	{:else if project.visual === 'archive'}
		<div
			class="technical archive"
			role="img"
			aria-label="HexSolve programming archive illustration: fundamentals lead into algorithms and data structures."
		>
			<div class="visual-label">
				<span class="tiny-square"></span> PROGRAMMING, ORGANIZED <span>{'{ }'}</span>
			</div>
			<div class="archive-flow">
				<div class="code-window" aria-hidden="true">
					<span>for ( )</span>
					<i></i><i></i><i></i>
				</div>
				<div class="topic-route">
					<span><i></i> Fundamentals</span><span class="route-line"></span><span
						><i></i> Search &amp; sort</span
					><span class="route-line"></span><span><i></i> DSA</span>
				</div>
			</div>
			<div class="visual-bottom"><span>LEARN. SOLVE. REVISIT.</span><span>HexSolve</span></div>
		</div>
	{/if}
</div>

<style>
	.project-visual {
		background: #dfe6e8;
		padding: 30px;
		aspect-ratio: 1.85;
		display: flex;
		align-items: center;
		justify-content: center;
		overflow: hidden;
		border-bottom: 1px solid #bcc8d4;
	}
	img {
		width: 100%;
		height: 100%;
		object-fit: contain;
		border-radius: 4px;
		filter: drop-shadow(0 5px 8px #182a4120);
	}
	.featured {
		padding: 35px;
		aspect-ratio: auto;
		min-height: 360px;
		border-bottom: 0;
		background: #d7e2f4;
	}
	.dark {
		background: #dce2df;
	}
	.compact {
		padding: 14px;
		aspect-ratio: auto;
		min-height: 180px;
		border-bottom: 0;
	}
	.technical {
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		justify-content: space-between;
	}
	.visual-label,
	.visual-bottom {
		display: flex;
		align-items: center;
		gap: 8px;
		font: 9px var(--mono);
		letter-spacing: 1px;
		color: #34465f;
	}
	.visual-label > span:last-child,
	.visual-bottom > span:last-child {
		margin-left: auto;
	}
	.tiny-square {
		width: 6px;
		height: 6px;
		background: var(--blue);
	}
	.judge-flow {
		display: flex;
		justify-content: space-around;
		align-items: center;
		gap: 8px;
		padding: 20px 0;
	}
	.code-symbol,
	.judge-node,
	.verdict {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 12px;
		font: 27px var(--mono);
		color: var(--blue);
	}
	.code-symbol > span,
	.judge-node > span:last-child,
	.verdict > span:last-child {
		font: 10px var(--mono);
		color: #34465f;
	}
	.brackets {
		display: grid;
		place-items: center;
		width: 66px;
		height: 52px;
		background: var(--cream);
		border: 2px solid var(--ink);
		border-radius: 6px;
		box-shadow: 4px 4px 0 var(--ink);
		font-size: 23px;
	}
	.connector {
		color: #51483e;
		font-size: 20px;
	}
	.verdict > span:first-child {
		border: 2px solid var(--ink);
		border-radius: 50%;
		width: 38px;
		height: 38px;
		display: grid;
		place-items: center;
		font-size: 22px;
	}
	.archive-flow {
		display: flex;
		align-items: center;
		justify-content: space-evenly;
		gap: 24px;
		padding: 18px 0;
	}
	.code-window {
		width: 104px;
		min-height: 76px;
		border: 2px solid #344b42;
		border-radius: 7px;
		position: relative;
		padding: 18px 14px 12px;
		background: var(--cream);
		box-shadow: 5px 5px 0 #344b42;
		font: 15px var(--mono);
		color: var(--blue);
	}
	.code-window::before {
		content: '';
		position: absolute;
		top: 7px;
		left: 10px;
		width: 5px;
		height: 5px;
		border-radius: 50%;
		background: var(--coral);
		box-shadow:
			9px 0 0 #d1a748,
			18px 0 0 #739b7d;
	}
	.code-window i {
		display: block;
		height: 3px;
		margin-top: 8px;
		background: #91a3ae;
	}
	.code-window i:nth-of-type(1) {
		width: 72%;
	}
	.code-window i:nth-of-type(2) {
		width: 88%;
		margin-left: 9px;
	}
	.code-window i:nth-of-type(3) {
		width: 55%;
		margin-left: 9px;
	}
	.topic-route {
		font: 11px var(--mono);
		color: #34465f;
	}
	.topic-route > span {
		display: flex;
		align-items: center;
		gap: 10px;
	}
	.topic-route i {
		width: 6px;
		height: 6px;
		border: 1px solid var(--blue);
		border-radius: 50%;
	}
	.route-line {
		height: 17px;
		border-left: 1px solid #645b4d;
		margin-left: 2px;
	}
	@media (max-width: 950px) {
		.featured {
			min-height: 290px;
			padding: 25px;
		}
		.project-visual:not(.featured):not(.compact) {
			padding: 24px;
		}
		.visual-label,
		.visual-bottom {
			font-size: 8px;
			letter-spacing: 0.4px;
		}
	}
	@media (max-width: 600px) {
		.featured {
			min-height: 0;
			aspect-ratio: 1.6;
			padding: 22px;
		}
		.compact {
			min-height: 0;
			aspect-ratio: 2.2;
			padding: 18px;
		}
	}
</style>
