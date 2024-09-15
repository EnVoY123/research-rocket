<template>
  <div class="login">
    <h2>Вход в личный кабинет</h2>
    <form @submit.prevent="login">
      <div>
        <label>Email</label>
        <input v-model="email" type="email" required />
      </div>
      <div>
        <label>Пароль</label>
        <input v-model="password" type="password" required />
      </div>
      <button type="submit">Войти</button>
    </form>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      error: '',
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('/login', { email: this.email, password: this.password });
        // Предполагается, что сервер возвращает токен авторизации
        localStorage.setItem('token', response.data.token);
        this.$router.push('/dashboard');
      } catch (error) {
        this.error = 'Ошибка входа. Проверьте свои данные.';
      }
    },
  },
};
</script>

<style scoped>
.login {
  max-width: 400px;
  margin: 0 auto;
  text-align: center;
}
form div {
  margin-bottom: 10px;
}
button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
}
</style>
