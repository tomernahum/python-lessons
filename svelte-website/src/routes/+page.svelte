<script>
	import Bubble from "$lib/Bubble.svelte";
	import Section from "$lib/Section.svelte";
	import SectionHeader from "$lib/SectionHeader.svelte";

    import "./page.css"

	

    const test = Bubble

</script>


<h1> TN Python Lessons Curriculum</h1>

<Section>
    <Bubble title="Stats">
        <p>
            Extra Credit:&nbsp; 40 pts
        </p>
        <p style="margin-top:30px">
            (At 100 points of EC you will get a free slice of pizza)
        </p>
    </Bubble>

    <Bubble title="Resources">
        <li>
            <a href="https://www.py4e.com/lessons">
                Py4e Curriculum / Slides</a>
        </li>
        <li>
            <a href="https://automatetheboringstuff.com/2e/">"Textbook"</a>
        </li>

        <li>
            <a href="https://www.w3schools.com/python/python_operators.asp">Python Operators</a>
        </li>
    </Bubble>

</Section>

<br>

<Section title="Yes">
    <Bubble title="Test"> Testing </Bubble>
    <Bubble title="Test"> Testing </Bubble>
    <Bubble title="Test"> Testing </Bubble>
    <Bubble title="Test"> Testing </Bubble>
    <Bubble title="Test"> Testing </Bubble>
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
        margin-bottom:100px;
    }
    
</style>