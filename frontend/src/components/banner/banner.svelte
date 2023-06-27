<script>

	import Title from "@/components/type/title.svelte";

</script>
<style>
  .banner {
    margin: 0;
    padding: 10vh 0;
    color: rgb(234, 249, 205);
    background: rgb(29, 138, 53);
  }
  .display {
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  }
  .individual {
    margin: 2em;
    font-size: 1.5em;
    text-align: center;
    max-width: 50%;
    margin: 2em auto;
  }
  .community {
    margin: 3em auto;
    text-align: center;
    font-style: italic;
    /* blake's got a new face */
  }
</style>

<div class="banner display">
  <Title><h2>Distributed toolshare</h2></Title>
  <p class="individual">Stop buying things and leaving them in your garage all year</p>
  <p class="community">Share them with your neighbors, instead!</p>
</div>

