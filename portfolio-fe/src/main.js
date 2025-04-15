import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import 'material-design-icons-iconfont/dist/material-design-icons.css';

createApp(App)
  .use(vuetify)
  .use(createPinia())
  .use(router)
  .mount('#app');
