<script>
	import Title from "../type/title.svelte";

</script>
<style>
  .logo {
    font-size: 1rem;
  }
  .common {
    color: rgb(251, 197, 0);
  }
  .place {
    color: rgb(43, 197, 67);
  }
  .tools {
    color: rgb(0, 166, 212);
  }
  .link-list {
    color: #202020;
    list-style-type: none;
    display: inline-flex;
    gap: 1em;
    font-size: .625em;
    opacity: .7;
  }
  .link {
    font-weight: 600;
    font-family: inherit;
    color: inherit;
    text-decoration: none;
  }
  .link:hover {
    opacity: .7;
  }
  .sticky {
    position: sticky;
    top: 0;
    left: 0;
    background: white;
  }
  .header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    text-transform: uppercase;
    color: rgb(63, 141, 102);
    font-weight: 900;
    margin: 1em;
  }
</style>

<nav class="header sticky">
  <a class="link" href="/"><Title className="small"><span class="common">Common</span><span class="place">place</span><span class="tools">Tools</span></Title></a>
  <ul class="link-list">
    <li><a class="link tools" href="/tools">Tools</a></li>
    <li><a class="link login" href="/login">Login</a></li>
  </ul>
</nav>