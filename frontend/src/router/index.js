import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/components/HomePage.vue';
import Register from '@/components/RegisterPage.vue';
import ConfirmEmail from '@/components/EmailConfirmationPage.vue';
import Login from '@/components/LoginPage.vue';
import Dashboard from '@/components/DashboardPage.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/signup', name: 'Register', component: Register },
  { path: '/confirm-email', name: 'ConfirmEmail', component: ConfirmEmail },
  { path: '/login', name: 'Login', component: Login },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;