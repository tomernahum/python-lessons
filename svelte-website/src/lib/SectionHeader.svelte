<!-- Note: this needs to be wrapped in a container for the sticky to know when to stop sticking -->


<script lang="ts">
    export let text:string
</script>

<h2 class="sticky">
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

        margin-bottom: -14px;
        margin-top: 0;
        
    }


    h2 {
        font-size: 25px;
        font-size: 30px;
        text-decoration: underline;
    }
</style>

