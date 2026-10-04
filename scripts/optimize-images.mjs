import sharp from 'sharp';
import { writeFile } from 'node:fs/promises';
const names = ['taskora', 'wholocks', 'movies', 'tracker'];
const metadata = {};
for (const name of names) {
	const result = await sharp('static/projects/' + name + '.png')
		.resize({ width: 1400, withoutEnlargement: true })
		.webp({ quality: 83 })
		.toFile('static/projects/' + name + '.webp');
	metadata[name] = { width: result.width, height: result.height, bytes: result.size };
}
await writeFile('src/lib/data/image-sizes.json', JSON.stringify(metadata, null, 2) + '\n');
console.log(metadata);
