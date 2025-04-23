<template>
  <v-app>
    <v-navigation-drawer v-model="drawer" app clipped>
      <v-list dense>
        <v-list-item
          v-for="item in navItems"
          :key="item.title"
          link
          :to="item.route"
        >
          <v-icon color="surface-variant">{{ item.icon }}</v-icon>
          <v-list-item-title color="surface-variant">{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar>
      <v-app-bar-nav-icon @click="drawer = !drawer" />
      <v-toolbar-title color="surface-variant">My Portfolio</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <v-container>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    name: 'App',
    data () {
      return {
        drawer: false,
        navItems: [
          { title: 'Home', icon: 'mdi-home', route: '/' },
          { title: 'About', icon: 'mdi-information', route: '/about' },
          { title: 'Contact', icon: 'mdi-note-edit', route: '/contact' },
        ],
      }
    },
  }
</script>
