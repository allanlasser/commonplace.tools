<script>
	import Title from "@/components/type/title.svelte";

  export let data;
</script>

<style>
  dt, dd {
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size: .75em;
    padding: 0;
    margin: 0 0 1em 0;
  }
  dt {
    text-transform: uppercase;
    font-size: .5em;
    opacity: .5;
  }
  .grid {
    display: grid;
  }
  .grid.center {
    justify-content: center;
    align-items: center;
  }
  .grid-8em {
    grid-template-columns: repeat(auto-fit, minmax(8em, 1fr));
  }
  .grid-item {
    grid-column: span 1;
    grid-row: span 1;
  }
  .grid.center .grid-item {
    text-align: center;
  }
</style>

<Title>{data.tool.name}</Title>
<dl class="grid grid-8em center">
  {#if data.location}
  <div class="grid-item">
    <dt>Location</dt>
    <dd>{data.location.name}</dd>
  </div>
  {/if}
  {#if data.owner}
  <div class="grid-item">
    <dt>Owner</dt>
    <dd>{data.owner.username}</dd>
  </div>
  {/if}
  {#if data.status}
  <div class="grid-item">
    <dt>Status</dt>
    <dd>{data.status.name}</dd>
  </div>
  {/if}
</dl>