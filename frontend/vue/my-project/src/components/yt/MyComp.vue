<template>
  <div class="yt">
    <h1>{{ msg }}-{{ yt }}</h1>
    <h2>Essential Links</h2>
  </div>
</template>

<script>
export default {
  name: 'hello2',
  data () {
    return {
      msg: 'Hello YT',
      yt: 'ytest'
    }
  }
}
</script>

<style scoped>

h3 {
  color: blue;
}

</style>
