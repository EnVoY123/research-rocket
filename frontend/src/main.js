import { createApp } from 'vue';
import App from './components/App.vue';
import router from './router';
import axios from 'axios';

axios.defaults.baseURL = 'http://127.0.0.1:5000/';

createApp(App).use(router).mount('#app');
