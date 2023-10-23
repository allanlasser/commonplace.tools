<script lang="ts">
	import Tool from '@/components/tool';

	export let data;
</script>

<h1>{data.user.username}</h1>
<p>{data.user.first_name} {data.user.last_name}</p>
{#if data.tools}
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
{/if}

{#if data.loans}
	<h2>Loans</h2>
	{#if data.loans.results && data.loans.results.length > 0}
		<ul>
			{#each data.loans.results as loan}
				<li><p>{loan.lendable}</p></li>
			{/each}
		</ul>
	{:else}
		<div class="empty"><p>No loans</p></div>
	{/if}
{/if}
