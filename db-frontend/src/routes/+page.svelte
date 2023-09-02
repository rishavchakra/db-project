<script lang='ts'>
    import { onMount } from 'svelte';
    import Question1graph from './question1graph.svelte';
    import { SERVER_PUBLIC_IP } from '../constants';
    import { countryNames, regionNames } from '../stores';

    async function getCountryData() {
        // GET by default
        const response = await fetch(`${SERVER_PUBLIC_IP}/countries`);
        const data = await response.json();
        return data;
    }

    async function getRegionData() {
        const response = await fetch(`${SERVER_PUBLIC_IP}/regions`);
        const data = await response.json();
        return data;
    }

    async function getCountryByRegion(region: string) {
        const response = await fetch(`${SERVER_PUBLIC_IP}/countries/${region}`);
        const data = await response.json();
        return data;
    }

    async function getSuicideData() {
        const response = await fetch(`${SERVER_PUBLIC_IP}/suicides`);
        const data = await response.json();
        return data;
    }

    // Load initial data from the API
    onMount(async () => {
        const countryData = await getCountryData();
        countryData.forEach(( countryData: any ) => {
            $countryNames[countryData.id] = countryData.name
        });
        console.log($countryNames)

        const regionData = await getRegionData();
        regionData.forEach(( region: any ) => {
            $regionNames.push(region.name);
        });
        console.log($regionNames)
    })
</script>

<h1>Welcome to SvelteKit</h1>

<Question1graph />
