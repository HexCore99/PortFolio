import type { AssetPath } from '$app/types';
export type Project = {
	id: string;
	title: string;
	summary: string;
	detail: string;
	category: string;
	tags: string[];
	repositoryUrl: string;
	releaseUrl?: string;
	image?: { src: AssetPath; alt: string; width: number; height: number };
	featured: boolean;
	additional?: boolean;
	visual?: 'judge' | 'gear';
};

export const profile = {
	name: 'Siabul Hassan',
	role: 'Software Developer',
	email: 'siabulhassan@gmail.com',
	github: 'https://github.com/HexCore99/',
	linkedin: 'https://www.linkedin.com/in/siabul-hassan/'
};

export const projects: Project[] = [
	{
		id: 'taskora',
		title: 'Taskora',
		category: 'Desktop · Productivity',
		summary: 'Local-first Kanban for focused personal work.',
		detail:
			'Projects, boards, and task details in one desktop workspace. Built with a Rust backend and SQLite storage to keep your work on your own device.',
		tags: ['Tauri 2', 'Rust', 'React', 'SQLite', 'Zustand'],
		repositoryUrl: 'https://github.com/HexCore99/Taskora',
		releaseUrl: 'https://github.com/HexCore99/Taskora/releases/latest',
		image: {
			src: 'projects/taskora.png',
			alt: 'Taskora desktop app with a project sidebar and Todo, In Progress, and Completed Kanban columns.',
			width: 1715,
			height: 1022
		},
		featured: true
	},
	{
		id: 'wholocks',
		title: 'WhoLocks',
		category: 'Windows · Developer utility',
		summary: 'Find the process standing between you and your files.',
		detail:
			'A Windows utility that identifies processes locking files or folders, with File Explorer integration and both CLI and GUI workflows.',
		tags: ['Rust', 'Windows', 'File-system tools', 'CLI', 'Desktop'],
		repositoryUrl: 'https://github.com/HexCore99/wholocks',
		releaseUrl: 'https://github.com/HexCore99/wholocks/releases/latest',
		image: {
			src: 'projects/wholocks.png',
			alt: 'WhoLocks showing process names, file paths, and process IDs for a selected folder in Windows File Explorer.',
			width: 1113,
			height: 701
		},
		featured: false
	},
	{
		id: 'quickjudge',
		title: 'QuickJudge',
		category: 'Full-stack · Competitive programming',
		summary: 'From a programming problem to a judged submission.',
		detail:
			'A full-stack online judge and programming-contest platform with problem sets, submissions, leaderboards, and authenticated student and admin workflows.',
		tags: ['React', 'Express', 'MySQL', 'Redux Toolkit', 'JWT'],
		repositoryUrl: 'https://github.com/HexCore99/QuickJudge',
		visual: 'judge',
		featured: false
	},
	{
		id: 'gearguard',
		title: 'GearGuard',
		category: 'Web application · Equipment management',
		summary: 'An organized approach to university sports equipment.',
		detail:
			'Track availability, equipment health, and maintenance needs through a clear checkout experience for university students and staff.',
		tags: ['React', 'Vite', 'Tailwind CSS', 'React Router'],
		repositoryUrl: 'https://github.com/HexCore99/GearGuard',
		visual: 'gear',
		featured: false
	},
	{
		id: 'movies',
		title: 'Neural Movie Recommender',
		category: 'Machine learning · Movie discovery',
		summary: 'Connecting learned preferences with the next movie.',
		detail:
			'A movie discovery app powered by neural collaborative filtering. A TensorFlow/Keras model connects to a Flask API and Next.js interface for browsing and recommendations.',
		tags: ['Python', 'TensorFlow/Keras', 'Flask', 'Next.js'],
		repositoryUrl: 'https://github.com/HexCore99/neural-movie-recommender',
		image: {
			src: 'projects/movies.png',
			alt: 'Neural Movie Recommender browser with a title search and movie cards for Toy Story, Jumanji, Grumpier Old Men, and Waiting to Exhale.',
			width: 1900,
			height: 945
		},
		featured: false
	},
	{
		id: 'snake',
		title: 'Don’t Be a Snake',
		category: 'Game development',
		summary:
			'A C++/raylib game with gameplay states, sound, scoring, and Windows and Linux builds.',
		detail: '',
		tags: ['C++', 'raylib', 'Windows / Linux'],
		repositoryUrl: 'https://github.com/HexCore99/Snake-Game',
		image: {
			src: 'projects/snake.png',
			alt: 'Don’t Be a Snake gameplay showing the snake and food on a dark tiled grid, with the score in the corner.',
			width: 1204,
			height: 805
		},
		featured: false,
		additional: true
	},
	{
		id: 'clock',
		title: '7 Segment Digital Clock',
		category: 'Graphics programming',
		summary:
			'A C++/raylib clock with custom seven-segment rendering and a real-time, 12-hour display.',
		detail: '',
		tags: ['C++', 'raylib', 'Custom rendering'],
		repositoryUrl: 'https://github.com/HexCore99/digital_clock',
		image: {
			src: 'projects/clock.png',
			alt: 'Digital Clock application displaying the time in custom red seven-segment digits on a black background.',
			width: 805,
			height: 477
		},
		featured: false,
		additional: true
	}
];

export const skills = [
	{
		title: 'Web & interfaces',
		number: '01',
		items: ['React', 'Next.js', 'Tailwind CSS', 'Zustand', 'Redux Toolkit']
	},
	{
		title: 'Desktop & systems',
		number: '02',
		items: ['Rust', 'Tauri', 'C++', 'raylib', 'Windows tooling']
	},
	{
		title: 'Backend & data',
		number: '03',
		items: ['Express', 'SQLite', 'MySQL', 'Python', 'Flask', 'TensorFlow/Keras']
	}
];
