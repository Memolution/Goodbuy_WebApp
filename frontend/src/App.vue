<template>
  <div id="app">
    <v-main>
      <router-view />
    </v-main>
    <Navigation></Navigation>
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
