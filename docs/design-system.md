# Portfolio design

Cream (#f6f3ea), navy (#182a41), cobalt (#2854c5), and peach (#f6a57f).
The restored layout uses a wide featured project, two-column project grid, supporting builds, and a navy contact panel.

Neo Svelte supplies the shared action buttons, navigation controls, and skill pills. Its system font stack is used throughout; no external font requests are made. Skill pills are non-interactive labels, not pretend buttons or proficiency ratings.

Numbered section captions and redundant hero micro-labels are omitted. The hero features a floating Taskora window, code card, and monogram, with pause and reduced-motion support. Project cards reveal once as they enter the viewport. Source screenshots remain local. Project and contact content lives in src/lib/data/portfolio.ts.
