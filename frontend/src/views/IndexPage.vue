<template>
  <div id='index'>
    <div id='parent'>
      <template>
        <Indexpage></Indexpage>
      </template>
    </div>
  </div>
</template>

<script>
import Indexpage from '@/components/IndexPage.vue'
export default {
  name: 'IndexPage',
  components: {
    Indexpage
  }
}
</script>
