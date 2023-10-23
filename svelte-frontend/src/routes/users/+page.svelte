<script>
	import Title from '@/components/type/title.svelte';

	export let data;
</script>

<Title><h1>Users</h1></Title>
<ul>
	{#each data.users.results as { id, username }}
		<li><a href="/users/{id}">{username}</a></li>
	{/each}
</ul>
