<template>
<v-app>
  <WillForm />
</v-app>
</template>

<script>
// @ is an alias to /src
import WillForm from '@/components/WillForm.vue'
export default {
  name: 'Will',
  data: () => ({
  }),
  components: {
    WillForm
  }
}
</script>
