<template>
  <div class="home">
    <header>
      <h1>Инсайт Приложение</h1>
      <div class="actions">
        <router-link to="/login" class="btn">Войти в кабинет</router-link>
        <router-link to="/signup" class="btn">Зарегистрироваться</router-link>
      </div>
    </header>

    <section class="intro">
      <h2>Выявляйте проблемы и инсайты на основе интервью</h2>
      <p>Помогает в проведении кодирования, анализа и построении рекомендаций.</p>
    </section>

    <section class="features">
      <div class="feature">
        <h3>Анализ данных</h3>
        <p>Мощный инструмент анализа данных интервью.</p>
      </div>
      <div class="feature">
        <h3>Построение персон</h3>
        <p>Создавайте точные персоны на основе данных.</p>
      </div>
    </section>
  </div>
</template>

<style scoped>
.home {
  text-align: center;
}
.actions {
  display: flex;
  justify-content: flex-end;
  margin-top: 20px;
}
.btn {
  margin-left: 10px;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  text-decoration: none;
  border-radius: 5px;
}
.intro {
  margin-top: 50px;
}
.features {
  display: flex;
  justify-content: space-around;
  margin-top: 50px;
}
.feature {
  max-width: 300px;
}
</style>
