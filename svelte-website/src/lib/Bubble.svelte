<script lang="ts">
	import { onMount } from "svelte";


    export let open:boolean = false;
    export let title:string;

    
    // Bug: will share the state among bubbles with the same title. // only way i can think of to make a unique id is to generate one from the dom. This is too much work for now
    const id = title
    let ready = false;
    onMount(()=>{
        const saved_state = sessionStorage.getItem(id)

        if (saved_state) {
            // console.log("WOW SAVED STATE", saved_state)
            if (saved_state==="1")
                open = true
            else
                open = false
            
                ready=true;
        }

        else {
            // console.log("saving onmount")
            // saveState()
            ready=true
        }

    })
    function saveState(){
        if (typeof sessionStorage === "undefined" || !sessionStorage){
            return
        }
        
        if (open) 
            sessionStorage.setItem(id, "1")
        else
            sessionStorage.setItem(id, "0")
    }
    $: {
        open
        if (ready)
            saveState()
    }


</script>


<details bind:open={open}>
    <summary>
        <h3 style="display:inline">
            {title}
        </h3>
    </summary>
    
    <section>
        <slot />
    </section>
    
</details>


<style>
    details {
        margin-top: 20px;
        margin-bottom: 20px;;

        padding: 10px;
        padding-left: 10px;
        padding-right: 10px;
        /* padding-left: 55px; */

        border: 2px solid black;
        border-radius: 10px;
    }

    details > summary {
        margin-left: 0px; 
        
        padding-bottom: 3px;
    }

    details > summary > h3 {
        margin-left: 7px;
    }

    details > section {
        margin-left: 3.5px;
        /* padding-left: 20px;
        padding-left: 55px; */
        padding-left: 35px;
        
        padding-right: 5px;

        padding-top: 1px;

        /* border-left: 2px solid rgb(109, 109, 109); */


        padding-top: 15px;
        padding-bottom: 5px;
    }

    
    details > section > :global(*:first-child) {
        margin-top:15px;
    }

    details > section > :global(*:last-child){
        margin-bottom: 5px;

        /* border-left: 2px solid rgb(109, 109, 109); */
    }

    



    h3 {
        font-size: 25px;
        font-size: 30px;
        text-decoration: underline;
    }
</style>