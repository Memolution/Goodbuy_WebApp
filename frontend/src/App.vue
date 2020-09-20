<template>
  <div id="app">
    <Navigation></Navigation>
    <v-main>
      <router-view />
    </v-main>
  </div>
</template>

<script>
import Navigation from './components/Navigation'
export default {
  name: 'App',
  components: {
    Navigation
  }
}
</script>
