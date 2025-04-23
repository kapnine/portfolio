<template>
  <v-container class="fill-height" max-width="900">
    <div>
      <v-img
        class="mb-4"
        height="150"
        src="@/assets/DeepOceanWave.svg"
      />

      <div class="mb-8 text-center">
        <div class="text-body-2 font-weight-light mb-n1">Portfolio of</div>
        <h1 class="text-h2 font-weight-bold">Justin Kapacinskas</h1>
      </div>

      <v-row>
        <v-col cols="12">
          <v-card
            class="py-4"
            color="surface-variant"
            prepend-icon="mdi-code-block-tags"
            rounded="lg"
            variant="tonal"
          >
            <template #title>
              <h2 class="text-h5 font-weight-bold">
                Technologies used
              </h2>
            </template>

            <template #subtitle>
              <div class="text-subtitle-1">
                <!-- Change this page by updating <v-kbd>{{ `<HelloWorld />` }}</v-kbd> in <v-kbd>components/HelloWorld.vue</v-kbd>. -->
                <p class="mb-0">
                  This portfolio is built using the following technologies:
                </p>
                <ul class="mb-0">
                  <li>Vue 3</li>
                  <li>Vuetify 3</li>
                  <li>Vue Router</li>
                  <li>Vite</li>
                  <li>Django</li>
                  <li>Django REST Framework</li>
                  <li>Docker</li>
                  <li>Azure DevOps</li>
                  <li>GitHub</li>
                  <li>Postgres</li>
                </ul></div>
            </template>
          </v-card>
        </v-col>

        <v-col v-for="link in links" :key="link.href" cols="6">
          <v-card
            append-icon="mdi-open-in-new"
            class="py-4"
            color="surface-variant"
            :href="link.href"
            :prepend-icon="link.icon"
            rel="noopener noreferrer"
            rounded="lg"
            :subtitle="link.subtitle"
            target="_blank"
            :title="link.title"
            variant="tonal"
          />
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script setup>
  const links = [
    {
      href: 'https://vuetifyjs.com/',
      icon: 'mdi-text-box-outline',
      subtitle: 'Learn about all things Vuetify in our documentation.',
      title: 'Documentation',
    },
    {
      href: 'https://vuetifyjs.com/introduction/why-vuetify/#feature-guides',
      icon: 'mdi-star-circle-outline',
      subtitle: 'Explore available framework Features.',
      title: 'Features',
    },
    {
      href: 'https://vuetifyjs.com/components/all',
      icon: 'mdi-widgets-outline',
      subtitle: 'Discover components in the API Explorer.',
      title: 'Components',
    },
    {
      href: 'https://discord.vuetifyjs.com',
      icon: 'mdi-account-group-outline',
      subtitle: 'Connect with Vuetify developers.',
      title: 'Community',
    },
  ]
</script>
