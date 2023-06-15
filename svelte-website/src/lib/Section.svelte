<script lang="ts">
	import SectionHeader from "./SectionHeader.svelte";

	export let title:string|null = null;
</script>

<div id={title}>
    {#if title} 
        <SectionHeader text={title} />
    {/if}
    <slot />
</div>

<style>
    /* The styling in regards to using margin and padding in this whole app could probably be a lot better. I think I am using it all wrong */
    /* I do feel like these components should maybe be stylable with margin and padding by default without extra work... does any frameworks do that? */

    div {
        --margin-bottom: var(--header-margin-bottom, -14px)
    }


    

</style>