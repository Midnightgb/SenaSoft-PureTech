import { createApp } from 'vue'
import App from './App.vue'
import router from './router'



// Plugins
import pinia from '@/plugins/pinia'

// Styles
import '@/style.css'

const app = createApp(App)

app.use(pinia)
app.use(router)

app.mount('#app')