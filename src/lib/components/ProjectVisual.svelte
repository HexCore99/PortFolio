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
	{:else if project.visual === 'gear'}
		<div
			class="technical gear"
			role="img"
			aria-label="GearGuard workflow illustration: equipment inventory connects to checkout and return."
		>
			<div class="visual-label">
				<span class="tiny-square"></span> EQUIPMENT, IN CIRCULATION <span>↻</span>
			</div>
			<div class="gear-flow">
				<div class="equipment">
					<div class="ball"></div>
					<div class="racket"></div>
				</div>
				<div class="gear-route">
					<span><i></i> Inventory</span><span class="route-line"></span><span><i></i> Checkout</span
					><span class="route-line"></span><span><i></i> Return</span>
				</div>
			</div>
			<div class="visual-bottom"><span>TRACK. CHECK OUT. RETURN.</span><span>GearGuard</span></div>
		</div>
	{/if}
</div>

<style>
	.project-visual {
		background: #d6bca0;
		padding: 30px;
		aspect-ratio: 1.85;
		display: flex;
		align-items: center;
		justify-content: center;
		overflow: hidden;
		border-bottom: 2px solid var(--ink);
	}
	img {
		width: 100%;
		height: 100%;
		object-fit: contain;
		border-radius: 2px;
		filter: drop-shadow(3px 3px 0 #111111);
	}
	.featured {
		padding: 35px;
		aspect-ratio: auto;
		min-height: 360px;
		border-bottom: 0;
		background: #d4b197;
	}
	.dark {
		background: #929359;
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
		color: #302b25;
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
		color: #302b25;
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
	.gear-flow {
		display: flex;
		align-items: center;
		justify-content: space-evenly;
		gap: 24px;
		padding: 18px 0;
	}
	.equipment {
		display: flex;
		align-items: center;
		gap: 16px;
	}
	.ball {
		height: 68px;
		width: 68px;
		border: 2px solid #344b42;
		border-radius: 50%;
		position: relative;
		overflow: hidden;
	}
	.ball::before {
		content: '';
		position: absolute;
		inset: 0 18px;
		border-left: 1px solid #344b42;
		border-right: 1px solid #344b42;
		border-radius: 50%;
	}
	.ball::after {
		content: '';
		position: absolute;
		top: 33px;
		left: 0;
		width: 100%;
		border-top: 1px solid #344b42;
		transform: rotate(-30deg);
	}
	.racket {
		width: 39px;
		height: 50px;
		border: 2px solid #344b42;
		border-radius: 50%;
		position: relative;
		margin-bottom: 27px;
		transform: rotate(25deg);
		background: #9cad86;
	}
	.racket::after {
		content: '';
		position: absolute;
		height: 32px;
		width: 4px;
		background: #344b42;
		left: 16px;
		top: 46px;
		border-radius: 3px;
	}
	.gear-route {
		font: 11px var(--mono);
		color: #302b25;
	}
	.gear-route > span {
		display: flex;
		align-items: center;
		gap: 10px;
	}
	.gear-route i {
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
