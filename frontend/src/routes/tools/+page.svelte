<script>
  import Title from '@/components/type/title.svelte';
  export let data;
</script>

<Title><h1>Tools</h1></Title>
<ul>
  {#each data.tools.results as {id, name}}
    <li><a href="/tools/{id}">{name}</a></li>
  {/each}
</ul>