<script setup>
import Aside from './components/Aside.vue';
import Bside from './components/Bside.vue';
import Footer from './components/Footer.vue';
import Header from './components/Header.vue';
import MainContent from './components/MainContent.vue';
</script>

<template>
  <div class="body">
    <Header />

    <main class="main-container">
        <div class="content-container">
            <div class="title">
                <h1>
                  <img 
                  src="./assets/images/Smugs-Conquest-Title.png" 
                  alt="title" 
                  class="titleimg"
                  />
                </h1>
            </div>
            <div class="leaderboard-container">
              <Aside />
              <MainContent />
              <Bside />
            </div>
        </div>
    </main>

    <Footer />

  </div>
</template>

<style scoped>
.body {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: var(--spacing-large) 0;
  background-image: url(./assets/images/s7background.png);
  background-size: cover;
  background-attachment: fixed;
  background-position: center;
  position: relative;
  padding-bottom: var(--spacing-xxlarge);
}

.main-container::before {
  content: '';
  position: absolute;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.7);
  z-index: 1;
  pointer-events: none;
}

.content-container {
  z-index: 2;
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
}

.title {
  display: flex;
  justify-content: center;
  font-family: 'Signika Negative', sans-serif;
  font-size: var(--font-size-xlarge);
  color: var(--white-color);
  margin-bottom: var(--spacing-medium);
}

.titleimg {
  height: 325px;
  position: relative;
  top: -30px;
}

.leaderboard-container {
  display: grid;
  grid-template-columns: 1fr minmax(1000px, auto) 1fr;
  gap: var(--spacing-large);
  align-items: flex-start;
}

.leaderboard-left {
  grid-column: 1;
}

.leaderboard {
  grid-column: 2;
  width: 100%;
}

.leaderboard-right {
  grid-column: 3;
}
</style>