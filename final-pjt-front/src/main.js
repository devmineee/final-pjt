import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
library.add(fas, far, fab)
const app = createApp(App)
const pinia = createPinia()
app.component('font-awesome-icon', FontAwesomeIcon)
pinia.use(piniaPluginPersistedstate)
app.use(pinia)
app.use(router)
app.mount('#app')
