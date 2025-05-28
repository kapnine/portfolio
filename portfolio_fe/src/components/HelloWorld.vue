<template>
  <v-row class="d-flex justify-center">
    <v-col cols="12" md="8">
      <v-img
        class="mb-4"
        height="150"
        src="@/assets/DeepOceanWave.svg"
      />

      <div class="text-body-2 font-weight-light mb-n1">Portfolio of</div>
      <h1 class="text-h2 font-weight-bold">Justin Kapacinskas</h1>
    </v-col>
    <v-col cols="12" md="8">
      <!-- <v-card class="mx-auto" max-width="300"> -->
      <v-card class="mx-auto">
        <v-list density="compact">
          <v-list-subheader
            color="accent"
          >
            <v-icon
              class="py-4"
              color="accent"
              rounded="lg"
              variant="tonal"
            >mdi-code-block-tags</v-icon>

            Technologies used for this portfolio:
          </v-list-subheader>

          <v-list-item
            v-for="(tech, t) in technologies"
            :key="t"
            color="primary-variant"
            :value="tech"
          >
            <template #prepend>
              <v-icon>{{ tech.icon }}</v-icon>
            </template>

            <v-list-item-title>{{ tech.name }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-card>
    </v-col>
  </v-row>
</template>

<script setup>

  const technologies = [
    { name: 'Vue 3', icon: 'mdi-vuejs' },
    { name: 'Vuetify 3', icon: 'mdi-vuetify' },
    { name: 'Vue Router', icon: 'mdi-router' },
    { name: 'Vite', icon: 'mdi-lightning-bolt' },
    { name: 'Django', icon: 'mdi-language-python' },
    { name: 'PyCharm', icon: 'mdi-code-braces' },
    { name: 'VS Code', icon: 'mdi-microsoft-visual-studio-code' },
    { name: 'Azure cloud computing', icon: 'mdi-microsoft-azure' },
    { name: 'Docker', icon: 'mdi-docker' },
    { name: 'GitHub', icon: 'mdi-github' },
    { name: 'Postgres', icon: 'mdi-database' },
  ];

  // const links = [
  //   {
  //     href: 'https://vuetifyjs.com/',
  //     icon: 'mdi-text-box-outline',
  //     subtitle: 'Learn about all things Vuetify in our documentation.',
  //     title: 'Documentation',
  //   },
  //   {
  //     href: 'https://vuetifyjs.com/introduction/why-vuetify/#feature-guides',
  //     icon: 'mdi-star-circle-outline',
  //     subtitle: 'Explore available framework Features.',
  //     title: 'Features',
  //   },
  //   {
  //     href: 'https://vuetifyjs.com/components/all',
  //     icon: 'mdi-widgets-outline',
  //     subtitle: 'Discover components in the API Explorer.',
  //     title: 'Components',
  //   },
  //   {
  //     href: 'https://discord.vuetifyjs.com',
  //     icon: 'mdi-account-group-outline',
  //     subtitle: 'Connect with Vuetify developers.',
  //     title: 'Community',
  //   },
  // ]
</script>
