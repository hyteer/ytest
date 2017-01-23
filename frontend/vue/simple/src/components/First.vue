<template>
  <div class="first">
    <h1>-{{ yt }}</h1>
    <h2>First Demo</h2>
    <p>
      {{ msg }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'first',
  data () {
    return {
      msg: 'This is the first demo,it i\'s cool!...',
      yt: 'YTest'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
