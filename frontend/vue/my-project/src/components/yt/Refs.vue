<template>
  <div id="parent">
    <h3>{{ title }}</h3>
  <user-profile ref="profile"></user-profile>
</div>
</template>

<script>
export default {
  name: 'refsdemo',
  data () {
    return {
      title: 'Refs Demo'
      msg: 'This is refs demo...'
    }
  }
}
</script>

<style scoped>

h3 {
  color: blue;
}

</style>
