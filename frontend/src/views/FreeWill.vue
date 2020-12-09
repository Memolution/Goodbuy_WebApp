<template>
<v-app>
  <FreeWillForm />

</v-app>
</template>

<script>
// @ is an alias to /src
import FreeWillForm from '@/components/FreeWillForm.vue'
export default {
  name: 'FreeWill',
  data: () => ({
  }),
  components: {
    FreeWillForm
  }
}
</script>
