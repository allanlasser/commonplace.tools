<script>
  export let className = '';
</script>

<style>
  .title {
    font-size: 2em;
    text-align: center;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    text-transform: uppercase;
    letter-spacing: .125em;
    font-weight: 900;
  }
  .small {
    font-size: 1rem;
  }
</style>

<span class="title {className}"><slot /></span>