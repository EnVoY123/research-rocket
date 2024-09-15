<template>
  <div class="signup">
    <h2>Регистрация</h2>
    <form @submit.prevent="signup">
      <div>
        <label>Email</label>
        <input v-model="email" type="email" required />
      </div>
      <div>
        <label>Пароль</label>
        <input v-model="password" type="password" required />
      </div>
      <button type="submit">Зарегистрироваться</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      message: '',
    };
  },
  methods: {
    async signup() {
      try {
        await axios.post('/signup', { email: this.email, password: this.password });
        this.message = 'На вашу почту отправлена ссылка для подтверждения почты.';
      } catch (error) {
        this.message = 'Ошибка регистрации.';
      }
    },
  },
};
</script>

<style scoped>
.signup {
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
