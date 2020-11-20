<template>
  <v-app>
    <v-navigation-drawer app v-model="drawer" clipped>
      <v-container>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="title grey--text text--darken-2">
              Menu
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
        <v-list dense nav>
          <v-list-item v-for="nav_list in nav_lists" :key="nav_list.name" :to="nav_list.link">
            <v-list-item-icon>
              <v-icon>{{ nav_list.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ nav_list.name }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-container>
    </v-navigation-drawer>
    <v-app-bar color="primary" dark app clipped-left>
    <v-app-bar-nav-icon @click="drawer=!drawer">

      </v-app-bar-nav-icon>
        <v-toolbar-title>
          <!-- <v-btn to="/" text>Life Hack App</v-btn> -->
          Memolution App
        </v-toolbar-title>
      <v-spacer></v-spacer>

      <!-- <v-toolbar-items>
        <v-btn text>Create New Account</v-btn>
        <v-btn text>Login</v-btn>
      </v-toolbar-items> -->
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>

    <v-footer color="primary" dark app>
      Created by Sydney
    </v-footer>
  </v-app>

</template>

<script>
export default {
  data () {
    return {
      drawer: null,
      nav_lists: [
        { name: 'Home', icon: 'mdi-home', link: '/' },
        { name: 'Form', icon: 'mdi-content-save-edit', link: '/will' },
        { name: 'Questionnaire', icon: 'mdi-comment-question', link: '/question' },
        // { name: 'Todo List', icon: 'mdi-vuetify', link: '/todo' },
        // { name: 'Purchased List', icon: 'mdi-cogs', link: '/order' },
        // { name: 'Read List', icon: 'mdi-palette', link: '/read' },
        { name: 'About', icon: 'mdi-palette', link: '/about' }
      ]
    }
  }
}
</script>
