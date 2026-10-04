# Siabul Hassan — Portfolio

A responsive, single-page portfolio built with SvelteKit 3, TypeScript, Neo Svelte, plain CSS, and Bun. An original engineering-workbench visual direction combines warm ivory, ink blue, coral accents, tactile buttons, and a floating composition of Taskora, a code card, and a monogram.

## Local development

```sh
bun install
bun run dev
```

## Validate and build

```sh
bun run check
bun run lint
bun run build
bun run preview
```

The static adapter prerenders the complete page into `build/`. No backend, environment variables, external runtime data requests, or analytics are needed.

## Edit the content

- `src/lib/data/portfolio.ts` holds all project content, skill groups, and contact destinations.
- `src/lib/components/` contains the navigation, hero, section heading, skills, project card, project visual, icons, and footer.
- `src/routes/layout.css` contains the global design tokens, layout primitives, responsive rules, and reduced-motion settings.
- `src/routes/+page.svelte` composes the sections and contains page metadata.
- `static/projects/` contains screenshots copied from the project repositories. See [asset sources](docs/asset-sources.md).
- `static/favicon.svg` and `static/social-preview.png` are local identity assets.

Contact links use GitHub, the supplied LinkedIn profile (without its tracking query), and `mailto:siabulhassan@gmail.com`.

The hero composition has a pause/resume control and respects the system reduced-motion preference. The page includes a keyboard skip link, visible focus outlines, a mobile navigation disclosure with Escape support, semantic headings, descriptive image alternatives, and reduced-motion support. All project links are visible without hover.

No deployment domain has been assumed. If the site is later published, use the chosen public domain for absolute social-preview metadata URLs and a canonical URL.

No deployment, commit, or push is part of this implementation.
