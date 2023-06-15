
<script>
	import Bubble from "./Bubble.svelte";

    export let title = "Post"
    export let open = false
</script>


<Bubble title={title} open={open}>
    <slot />
</Bubble>

 
<style>
    div {
        background: red;
    }
    :global(p) {
        margin: 24px 0;
    }
</style>