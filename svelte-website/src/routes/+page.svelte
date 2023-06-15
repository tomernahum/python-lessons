<script lang="ts">
	import Bubble from "$lib/Bubble.svelte";
	import Section from "$lib/Section.svelte";
	import SectionHeader from "$lib/SectionHeader.svelte";

    import "./page.css"
	import { getHomeworkComponents, getLMComponents } from "$lib/contentGetter";
	import UnnamedSection from "./UnnamedSection.svelte";

	
    const homeworkComponents = getHomeworkComponents()
    const lessonMaterialComponents = getLMComponents()
</script>




<h1> TN Python Lessons Curriculum</h1>

<UnnamedSection />

<br>

<Section title="Lesson Materials/Recap">
    {#each lessonMaterialComponents as post}
        <svelte:component this={post} />
    {/each}
</Section>

<Section title="Homework">
    {#each homeworkComponents as post}
        <svelte:component this={post} />
    {/each}
</Section>




<br style="margin-top:1000px">


<style>
    h1 {
        /* font-size: 30px; */
        font-size: 42px;

        margin-top: 28px;
        margin-bottom: 28px;
    }

    li {
        /* margin-bottom:100px; */
    }
    
</style>