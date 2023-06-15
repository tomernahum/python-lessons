//gets all files as imports ussing the impor
function getXComponents<Type>(importModulesEagerViteFunction:()=>Record<string, unknown>){
    const out:Type[] = []; 

    const modules = importModulesEagerViteFunction()
    for (const key in modules) {
        const x:any = modules[key]
        out.push(x.default as Type)
    }

    return out
}

import type Lesson1 from "../content/homework/0past-homeworks.svelte";

//imports all files as svelte components from the content/homework directory
export function getHomeworkComponents(){
    return getXComponents<(typeof Lesson1)>( () =>
        import.meta.glob("../content/homework/*", {eager:true})
    )
}

//imports all files as svelte components from the content/lesson-materials directory
export function getLMComponents(){
    return getXComponents<(typeof Lesson1)>( () =>
        import.meta.glob("../content/lesson-materials/*", {eager:true})
    )
}



// let homeworks = getHomeworkComponents();
// let lesson_materials = getLMComponents();



// export function getAPost()