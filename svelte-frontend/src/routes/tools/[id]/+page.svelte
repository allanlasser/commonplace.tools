<script>
	import Title from '@/components/type/title.svelte';

	export let data;
</script>

<Title><h1>{data.tool.name}</h1></Title>
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
			<dd><a href="/users/{data.owner.id}">{data.owner.username}</a></dd>
		</div>
	{/if}
	{#if data.status}
		<div class="grid-item">
			<dt>Status</dt>
			<dd>{data.status.name}</dd>
		</div>
	{/if}
</dl>
{#if data.history}
	<h2>History</h2>
	<table class="loan-history">
		<thead>
			<tr>
				<td>Loaned To</td>
				<td>Loaned On</td>
				<td>Returned On</td>
			</tr>
		</thead>
		{#each data.history.results as loan}
			<tr>
				<td
					><a href="/users/{loan.borrowing_user_data?.id}">{loan.borrowing_user_data?.username}</a
					></td
				>
				<td>{new Date(loan.start_date).toDateString()}</td>
				<td>{new Date(loan.returned_datetime).toDateString()}</td>
			</tr>
		{/each}
	</table>
{/if}

<style>
	dt,
	dd {
		font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu,
			Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
		font-size: 0.75em;
		padding: 0;
		margin: 0 0 1em 0;
	}
	dt {
		text-transform: uppercase;
		font-size: 0.5em;
		opacity: 0.5;
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
	.loan-history td {
		padding: 0.5em;
	}
	.loan-history tr {
		border: 1px solid #ccc;
	}
</style>
