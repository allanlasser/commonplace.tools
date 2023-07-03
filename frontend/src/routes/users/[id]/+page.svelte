<script lang="ts">
	import Tool from '@/components/tool';

	export let data;
</script>

<h1>{data.user.username}</h1>
<p>{data.user.first_name} {data.user.last_name}</p>
<h2>Tools</h2>
{#if data.tools.results && data.tools.results.length > 0}
	<ul class="tool-list">
		{#each data.tools.results as tool}
			<li class="tool-list-item"><Tool {...tool} /></li>
		{/each}
	</ul>
{:else}
	<div class="empty"><p>No tools</p></div>
{/if}
