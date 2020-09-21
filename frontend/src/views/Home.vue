<template>
  <div class="home">
    <IndexPage />
  </div>
</template>

<script>
// @ is an alias to /src
import IndexPage from '@/components/IndexPage.vue'
export default {
  name: 'Home',
  components: {
    IndexPage
  }
}
</script>
