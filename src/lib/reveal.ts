import type { Action } from 'svelte/action';

/** Reveal once on entry; leave content visible without JavaScript or with reduced motion. */
export const reveal: Action<HTMLElement> = (node) => {
	const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
	if (preference.matches || !('IntersectionObserver' in window)) return;
	node.classList.add('reveal-pending');
	const observer = new IntersectionObserver(
		([entry]) => {
			if (entry.isIntersecting) {
				node.classList.remove('reveal-pending');
				node.classList.add('reveal-visible');
				observer.disconnect();
			}
		},
		{ threshold: 0.08 }
	);
	observer.observe(node);
	const revealFocused = () => {
		node.classList.remove('reveal-pending', 'reveal-visible');
		observer.disconnect();
	};
	node.addEventListener('focusin', revealFocused);
	const show = () => {
		if (preference.matches) revealFocused();
	};
	preference.addEventListener('change', show);
	return {
		destroy() {
			observer.disconnect();
			preference.removeEventListener('change', show);
			node.removeEventListener('focusin', revealFocused);
		}
	};
};
