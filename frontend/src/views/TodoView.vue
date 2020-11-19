<template>
<v-app>
  <TodoButton />
</v-app>
</template>

<script>
// @ is an alias to /src
import TodoButton from '@/components/TodoButton.vue'
export default {
  name: 'Todo',
  data: () => ({
  }),
  components: {
    TodoButton
  }
}
</script>
