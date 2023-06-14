<script lang="ts">
	import SectionHeader from "./SectionHeader.svelte";

	export let title:string|null = null;
</script>

<div id={title}>
    {#if title} 
        <SectionHeader text={title}/>
    {/if}
    <slot />
</div>

<style>
    
</style>