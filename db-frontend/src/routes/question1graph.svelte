<script lang='ts'>
    import * as d3 from 'd3';
    import { countryNames, q1Data } from '../stores';
    import { onMount } from 'svelte';
    import type { countrySuicidesHappiness } from '$lib/datatypes';

    onMount(() => {
        let margin = {top: 10, right: 30, bottom: 30, left: 60};
        let width = 460 - margin.left - margin.right;
        let height = 450 - margin.top - margin.bottom;

        let q1Svg = d3.select('#graph-question1')
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)

        .append('g')
        .attr("transform", `translate(${margin.left}, ${margin.top})`);

        const x = d3.scaleLinear()
        .domain([0, 10])
        .range([0, width]);
        q1Svg.append('g')
            .attr("transform", `translate(0, ${height})`)
            .call(d3.axisBottom(x));

        const y = d3.scaleLinear()
        .domain([0, 100])
        .range([height, 0]);
        q1Svg.append('g')
            .call(d3.axisLeft(y));

        const tooltip = d3.select('#graph-question1')
        .append("div")
        .style("opacity", 0)
        .attr("class", "tooltip")
        .style("background-color", "white")
        .style("border", "solid")
        .style("border-width", "1px")
        .style("border-radius", "5px")
        .style("padding", "10px")

        const mouseover = (d: countrySuicidesHappiness) => tooltip
            .transition()
            .duration(200)
            .style('opacity', 1);
        const mousemove = (event: any, d: any) => tooltip
            .html(`${$countryNames[d.country]} has a suicide rate of ${d.suicides}`)
            // .html(`Country: ${d.country}, ${d.happinessScore}`)
            .style('left', (event.x)/2 + 'px')
            .style('top', (event.y)/2 + 'px')

        const mouseleave = () => tooltip
            .transition()
            .duration(200)
            .style('opacity', 0)

        q1Svg.append('g')
            .selectAll('dot')
            .data($q1Data)
            .enter()
            .append('circle')
            // Not a fan of using the any type...
            .attr('cx', (d: any) => x(d.happinessScore) )
            .attr('cy', (d: any) => y(d.suicides) )
            .attr('r', 3)
            .style('fill', '#69b3a2')
        .on('mouseover', mouseover)
        .on('mousemove', mousemove)
        .on('mouseleave', mouseleave)
    })
</script>

<div id="graph-question1"></div>
