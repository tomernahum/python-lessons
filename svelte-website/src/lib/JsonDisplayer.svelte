<script lang="ts">

    export let data:any;
    export let space = 4;
    export let width:string = "100%"
    export let maxHeight:string = "400px"

    export let style:string = ""
</script>

<div class="json-displayer" style={`width: ${width}; max-height:${maxHeight}; ${style}`}>
    {JSON.stringify(data, null, space)}
</div>


<style>
    div {
        white-space: pre;

        background: black;

        overflow-x: auto;
        overflow-y: auto;
        
    }

</style>