
<script lang="ts">
    
    import JsonDisplayer from "$lib/JsonDisplayer.svelte";
    // import type Lesson1 from "../content/homework/0past-homeworks.svelte";
	import { getHomeworkComponents, getLMComponents } from "$lib/contentGetter";

    
    //gets all files as imports from the vi
    // function getXComponents<Type>(importModulesEagerViteFunction:()=>Record<string, unknown>){
    //     const out:Type[] = []; 

    //     const modules = importModulesEagerViteFunction()
    //     for (const key in modules) {
    //         const x:any = modules[key]
    //         out.push(x.default as Type)
    //     }

    //     return out
    // }

    // //These function import all files as svelte components from the content/homework and content/lesson-materials directories
    // function getHomeworkComponents(){
    //     return getXComponents<(typeof Lesson1)>( () =>
    //         import.meta.glob("../content/homework/*", {eager:true})
    //     )
    // }
    // function getLMComponents(){
    //     return getXComponents<(typeof Lesson1)>( () =>
    //         import.meta.glob("../content/lesson-materials/*", {eager:true})
    //     )
    // }

    let homeworks = getHomeworkComponents();
    let lesson_materials = getLMComponents();

	
    

</script>

<br>
<br>


<h1>Hi</h1>



{#each homeworks as post}
    <svelte:component this={post} />
{/each}
<br>
{#each lesson_materials as post}
    <svelte:component this={post} />
{/each}
<br>




<br>
<br>

<!-- <Lesson1 /> -->