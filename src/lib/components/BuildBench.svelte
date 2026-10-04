<script lang="ts">
	import { NeoButton } from '@dvcol/neo-svelte/buttons';
	import { asset } from '$app/paths';
	let paused = $state(false);
</script>

<div class="creative-space" class:paused>
	<div
		class="composition"
		role="img"
		aria-label="A floating Taskora application window, a code card, and colorful software building blocks."
	>
		<div class="backplate" aria-hidden="true"></div>
		<svg class="spark" viewBox="0 0 100 100" aria-hidden="true"
			><path
				d="M50 0 58 32 85 15 68 42 100 50 68 58 85 85 58 68 50 100 42 68 15 85 32 58 0 50 32 42 15 15 42 32Z"
				fill="currentColor"
			/></svg
		>
		<div class="app-window">
			<div class="window-bar">
				<span class="window-dots"><i></i><i></i><i></i></span><span>Taskora</span><span
					class="window-mark">↗</span
				>
			</div>
			<img src={asset('projects/taskora.webp')} width="1400" height="834" alt="" />
		</div>
		<div class="code-card" aria-hidden="true">
			<div class="code-title">
				<span>&lt;/&gt;</span><span>Small ideas.<br />Working software.</span>
			</div>
			<div class="code-lines"><i></i><i></i><i></i><i></i></div>
			<span class="cursor"></span>
		</div>
		<div class="monogram" aria-hidden="true">sh<span>.</span></div>
		<div class="floating-tag tag-one" aria-hidden="true"><span>✳</span> Make it useful.</div>
		<svg class="scribble" viewBox="0 0 180 100" aria-hidden="true"
			><path d="M8 15C55 5 40 90 105 65S140 10 128 25s-4 63 42 54m-13-13 15 14-20 3" /></svg
		>
	</div>
	<div class="motion-control">
		<NeoButton
			class="motion-button"
			elevation={0}
			hover={0}
			active={0}
			scale={false}
			aria-pressed={paused}
			aria-label={paused ? 'Play hero animation' : 'Pause hero animation'}
			onclick={() => (paused = !paused)}>{paused ? 'Play motion ▷' : 'Pause motion Ⅱ'}</NeoButton
		>
	</div>
</div>

<style>
	.creative-space {
		min-width: 0;
		width: 100%;
		max-width: 570px;
		justify-self: center;
	}
	.composition {
		position: relative;
		aspect-ratio: 1.05;
		isolation: isolate;
	}
	.backplate {
		position: absolute;
		inset: 13% 4% 10% 8%;
		border-radius: 50% 42% 45% 38%;
		background: #e0e7f0;
		transform: rotate(-9deg);
	}
	.app-window {
		position: absolute;
		left: 7%;
		top: 23%;
		width: 88%;
		border: 1.5px solid var(--ink);
		border-radius: 10px;
		overflow: hidden;
		background: var(--white);
		box-shadow: 7px 9px 0 #182a4120;
		transform: rotate(-7deg);
		animation: window-drift 7s ease-in-out infinite;
	}
	.window-bar {
		height: 35px;
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 0 13px;
		border-bottom: 1px solid #c5ccd5;
		font-size: 11px;
		font-weight: 650;
	}
	.window-dots {
		display: flex;
		gap: 4px;
	}
	.window-dots i {
		width: 6px;
		height: 6px;
		border-radius: 50%;
		background: #afbac8;
	}
	.window-dots i:first-child {
		background: var(--coral);
	}
	.window-mark {
		font-size: 17px;
	}
	img {
		width: 100%;
		height: auto;
		display: block;
	}
	.code-card {
		position: absolute;
		left: 0;
		bottom: 4%;
		width: 56%;
		padding: 22px;
		background: var(--ink);
		color: var(--cream);
		border-radius: 12px;
		box-shadow: 6px 8px 0 #182a4120;
		transform: rotate(4deg);
		animation: code-drift 6s ease-in-out infinite;
	}
	.code-title {
		display: flex;
		align-items: center;
		gap: 14px;
		font-size: 14px;
		font-weight: 600;
		line-height: 1.5;
	}
	.code-title > span:first-child {
		font: 25px var(--mono);
		color: var(--coral);
	}
	.code-lines {
		display: grid;
		gap: 8px;
		margin-top: 20px;
	}
	.code-lines i {
		height: 5px;
		border-radius: 3px;
		background: #8199bd;
		width: 80%;
		transform-origin: left;
		animation: line-in 5s ease-in-out infinite;
	}
	.code-lines i:nth-child(2) {
		width: 57%;
		background: #f6a57f;
		animation-delay: 0.2s;
	}
	.code-lines i:nth-child(3) {
		width: 90%;
		animation-delay: 0.4s;
	}
	.code-lines i:nth-child(4) {
		width: 42%;
		background: #a3b699;
		animation-delay: 0.6s;
	}
	.cursor {
		display: block;
		width: 7px;
		height: 12px;
		background: var(--coral);
		margin-top: 12px;
		animation: blink 1.4s steps(2, end) infinite;
	}
	.monogram {
		position: absolute;
		right: 2%;
		bottom: 6%;
		width: 28%;
		aspect-ratio: 1;
		display: grid;
		place-content: center;
		background: var(--coral);
		border: 1.5px solid var(--ink);
		border-radius: 24px;
		box-shadow: 5px 6px 0 var(--ink);
		font-size: clamp(38px, 5vw, 68px);
		font-weight: 800;
		letter-spacing: -5px;
		transform: rotate(9deg);
		animation: badge-drift 5s ease-in-out infinite;
	}
	.monogram span {
		position: absolute;
		right: 19%;
		bottom: 15%;
		color: var(--blue);
	}
	.spark {
		position: absolute;
		right: 6%;
		top: 0;
		width: 18%;
		color: var(--blue);
		animation: spark-turn 24s linear infinite;
	}
	.floating-tag {
		position: absolute;
		top: 6%;
		left: 1%;
		display: flex;
		align-items: center;
		gap: 10px;
		background: var(--white);
		border: 1px solid var(--ink);
		border-radius: 30px;
		padding: 12px 18px;
		font-size: 14px;
		transform: rotate(-5deg);
		animation: tag-drift 6s ease-in-out infinite;
	}
	.floating-tag span {
		color: var(--blue);
		font-size: 22px;
	}
	.scribble {
		position: absolute;
		width: 30%;
		right: 2%;
		bottom: 34%;
		fill: none;
		stroke: var(--blue);
		stroke-width: 3;
		stroke-linecap: round;
		stroke-linejoin: round;
	}
	.motion-control {
		display: flex;
		justify-content: flex-end;
		margin-top: 20px;
	}
	.motion-control :global(.motion-button) {
		min-height: 44px;
		margin: 0;
		padding: 10px 13px;
		background: transparent;
		border: 1px solid #bec8d4;
		border-radius: 6px;
		font-size: 11px;
		color: var(--muted);
	}
	.paused *,
	.paused *::before {
		animation-play-state: paused !important;
	}
	@keyframes window-drift {
		50% {
			transform: translateY(-13px) rotate(-4deg);
		}
	}
	@keyframes code-drift {
		50% {
			transform: translateY(9px) rotate(1deg);
		}
	}
	@keyframes badge-drift {
		50% {
			transform: translateY(-12px) rotate(3deg);
		}
	}
	@keyframes tag-drift {
		50% {
			transform: translate(7px, -5px) rotate(-2deg);
		}
	}
	@keyframes spark-turn {
		to {
			transform: rotate(360deg);
		}
	}
	@keyframes line-in {
		0%,
		100% {
			transform: scaleX(0.75);
			opacity: 0.6;
		}
		35%,
		75% {
			transform: scaleX(1);
			opacity: 1;
		}
	}
	@keyframes blink {
		50% {
			opacity: 0;
		}
	}
	@media (max-width: 850px) {
		.creative-space {
			max-width: 490px;
		}
		.monogram {
			font-size: 60px;
		}
	}
	@media (max-width: 400px) {
		.code-card {
			padding: 14px;
		}
		.code-title {
			font-size: 11px;
			gap: 8px;
		}
		.code-title > span:first-child {
			font-size: 18px;
		}
		.code-lines {
			gap: 5px;
			margin-top: 12px;
		}
		.monogram {
			font-size: 42px;
			letter-spacing: -3px;
			border-radius: 17px;
		}
		.floating-tag {
			padding: 8px 12px;
			font-size: 12px;
		}
		.window-bar {
			height: 27px;
			font-size: 10px;
		}
	}
	@media (prefers-reduced-motion: reduce) {
		* {
			animation: none !important;
		}
		.motion-control {
			display: none;
		}
	}
</style>
