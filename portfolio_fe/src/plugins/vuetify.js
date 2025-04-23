/**
 * plugins/vuetify.js
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import '@mdi/font/css/materialdesignicons.css'
// import 'vuetify/styles'

// // Composables
// import { createVuetify } from 'vuetify'

// // https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
// export default createVuetify({
//   theme: {
//     defaultTheme: 'light',
//   },
// })

// plugins/vuetify.js
import 'vuetify/styles' // Make sure Vuetify styles are imported
import { createVuetify } from 'vuetify'

const deepOceanTheme = {
  dark: true, // Use dark mode to evoke a deep ocean ambiance
  colors: {
    background: '#001F3F',
    surface: '#003366',
    // surface: '#C4D8E2',
    primary: '#0077be',
    secondary: '#00BFFF',
    // accent: '#40E0D0',
    accent: '#C4D8E2',
    error: '#FF5252',
    info: '#2196F3',
    success: '#4CAF50',
    warning: '#FFC107',
  },
}

const vuetify = createVuetify({
  theme: {
    defaultTheme: 'deepOcean',
    themes: {
      deepOcean: deepOceanTheme,
    },
  },
})

export default vuetify
