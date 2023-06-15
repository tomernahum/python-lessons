<script>
	import Bubble from "$lib/Bubble.svelte";


	import Section from "$lib/Section.svelte";


    import turing_thumb from "../content/images/youtube-thumbnail-turing-complete-game-of-life.jpg"
    import cs50_thumb from "../content/images/youtube-thumbnail-cs50-python.png"

    // <!-- https://css-tricks.com/lazy-load-embedded-youtube-videos/ -->
    //could make into a component i guess but why bother
    const turingCompleteIframe = `<iframe
        style="vertical-align: top;"
        width="560"
        height="315"
        src="https://www.youtube-nocookie.com/embed/Kk2MH9O4pXY&autoplay=1"
        srcdoc="
            <style>*{padding:0;margin:0;overflow:hidden}html,body{height:100%}img,span{position:absolute;width:100%;top:0;bottom:0;margin:auto}span{height:1.5em;text-align:center;font:48px/1.5 sans-serif;color:white;text-shadow:0 0 0.5em black}</style>
            <a href=https://www.youtube-nocookie.com/embed/Kk2MH9O4pXY?autoplay=1>
                <img src=${turing_thumb}
                alt='Video Why is life turing complete?'>
                <span>▶</span>
            </a>"
        frameborder="0"
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
        title="Let’s BUILD a COMPUTER in CONWAY's GAME of LIFE ⠠⠵"
    ></iframe>`

    const cs50Iframe = `<iframe
        style="vertical-align: top;"
        width="560"
        height="315"
        src="https://www.youtube-nocookie.com/embed/5Jppcxc1Qzc&autoplay=1"
        srcdoc="
            <style>*{padding:0;margin:0;overflow:hidden}html,body{height:100%}img,span{position:absolute;width:100%;top:0;bottom:0;margin:auto}span{height:1.5em;text-align:center;font:48px/1.5 sans-serif;color:white;text-shadow:0 0 0.5em black}</style>
            <a href=https://www.youtube-nocookie.com/embed/5Jppcxc1Qzc?autoplay=1>
                <img src=${cs50_thumb}
                alt='CS50 - Lecture 6 - Python'>
                <span>▶</span>
            </a>"
        frameborder="0"
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
        title="CS50 - Lecture 6 - Python"
        loading="lazy"
    ></iframe>`

</script>
<Section>
    <Bubble title="Stats" open>
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

    <Bubble title="Bonus">
        <li>
            <a href="http://www.pythonchallenge.com/">http://www.pythonchallenge.com/</a>
        </li>
        
        <li>
            {@html turingCompleteIframe}
        </li>

        <li>
            {@html cs50Iframe}
        </li>


        <li>
            <a href="https://roadmap.sh/python">roadmap.sh</a>
        </li>
    </Bubble>
</Section>