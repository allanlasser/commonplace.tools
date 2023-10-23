<script lang="ts">
	export let id: number | string;
	export let name: string;
	export let lendable_status: string;
</script>

<div>
	<a href="/tools/{id}">{name}</a>
	<dl>
		<dt>Status</dt>
		<dd>{lendable_status}</dd>
	</dl>
</div>
