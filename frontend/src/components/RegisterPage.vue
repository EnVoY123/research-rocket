<template>
  <div class="register">
    <h1>Регистрация</h1>
    <form @submit.prevent="signup">
      <div>
        <label for="email">Email</label>
        <input v-model="email" type="email" id="email" required />
      </div>
      <div>
        <label for="password">Пароль</label>
        <input v-model="password" type="password" id="password" required />
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
        await axios.post('/register', {
          email: this.email,
          password: this.password,
        });
        this.message = 'На вашу почту отправлена ссылка для подтверждения почты.';
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style scoped>
.register {
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

div {
  margin-bottom: 10px;
}
</style>
