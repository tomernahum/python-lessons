<!-- Note: this needs to be wrapped in a container for the sticky to know when to stop sticking -->


<script lang="ts">
    export let text:string

    export let style=""
</script>

<h2 class="sticky" style={style}>
    {text}
</h2>

<style>
    .sticky {
        font-size: 30px;
        font-size: 36px;

        position: -webkit-sticky; 
        position:sticky; 
        top:0;

        background: white;
        padding: 2px;
        padding-bottom: 4px;
        padding-top:10px;

        margin-bottom: var(--margin-bottom, 0);
        margin-top: 0;
        
    }


    h2 {
        font-size: 25px;
        font-size: 30px;
        text-decoration: underline;
    }
</style>

