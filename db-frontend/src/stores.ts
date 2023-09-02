import type { countryID, countryIDName, countrySuicidesHappiness } from '$lib/datatypes';
import { writable, readable, type Writable } from 'svelte/store';

export const countryNames: Writable<countryIDName> = writable({})

export const regionNames: Writable<string[]> = writable([])

export const q1Data: Writable<countrySuicidesHappiness[]> = writable([
  { country: 1140, happinessScore: 4, suicides: 30 },
  { country: 1172, happinessScore: 6, suicides: 24 }
])
