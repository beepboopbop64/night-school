// The lessons catalog: the static index the shell navigates and searches.
// One entry per session; assembly does not maintain this (yet), so adding a
// session means adding a line here. Question-form titles per the show bible.

export interface CatalogEntry {
	slug: string;
	title: string;
	question: string;
	aha: string;
	minutes: number;
	status: 'live' | 'in-production';
}

export const catalog: CatalogEntry[] = [
	{
		slug: 'dotprod',
		title: 'The similarity meter',
		question: 'How do you score a match between two lists of numbers?',
		aha: 'The dot product is a similarity meter.',
		minutes: 12,
		status: 'live'
	},
	{
		slug: 'attention',
		title: 'The soft lookup table',
		question: 'How does a model decide which words matter to which?',
		aha: 'Attention is a soft lookup table.',
		minutes: 15,
		status: 'in-production'
	}
];
