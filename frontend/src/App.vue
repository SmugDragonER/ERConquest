<script>
import Footer from './components/Footer.vue';
import Header from './components/Header.vue';

export default {
    name: "App",
    data() {
        return {

        };
    },
    components: {
        Footer,
        Header,
    },
    watch: {

    },
    computed: {
        getClassForRoute() {
            switch (this.$route.path) {
                case "/": return "leaderboard";
                    break;
                case "/pickEm": return "pickEm";
                    break;
                default: return null;
            }
        }

    },
    methods: {
        setVhVariable() {
          let vh = window.innerHeight * 0.01;
          document.documentElement.style.setProperty('--vh', `${vh}px`);
        }
    },
    mounted() {
        // Attempt to fix mobile viewport height
        this.setVhVariable();

        window.addEventListener('resize', this.setVhVariable);
    }
}
</script>

<template>
  <Header />
  <div class="body">
    <main class="main-container">
        <div class="content-container">
            <div class="title-container">
                <h1 class="royal-header">
                  <div class="royal-top-row">
                    <span class="royal-text-top">
                        <span class="smugs-red">SMUG'S</span>
                        EU
                    </span>
                    <svg class="eu-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                      <g transform="translate(50,50)">
                        <path d="M0,-35 L2.5,-42 L-2.5,-42 Z M0,-38 L1.5,-33 L-1.5,-33 Z" transform="scale(0)" />
                        <g v-for="i in 12" :key="i" :transform="`rotate(${i * 30}) translate(0, -35)`">
                           <path d="M0,-4.5 L1.2,-1.2 L4.7,-1.2 L1.9,0.9 L2.9,4.2 L0,2.3 L-2.9,4.2 L-1.9,0.9 L-4.7,-1.2 L-1.2,-1.2 Z"
                                 fill="currentColor" stroke="var(--stroke-color)" stroke-width="2" />
                        </g>
                      </g>
                    </svg>
                  </div>
                  <span class="royal-bottom">CONQUEST</span>
                </h1>
                <img
                  src="/assets/images/s10title.png"
                  alt="Season 10 Royal"
                  class="season-img"
                />
            </div>

            <div :class="getClassForRoute + '-container'">
              <div :class="getClassForRoute">
                <router-view />
              </div>
            </div>
        </div>
    </main>

  </div>
  <Footer />
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&display=swap');

.body {
  /* USE THE JAVASCRIPT VARIABLE INSTEAD OF 100vh */
  /* Fallback for browsers without JS */
  min-height: 100vh;
  /* Height that accounts for mobile UI */
  min-height: calc(var(--vh, 1vh) * 100);

  display: flex;
  flex-direction: column;
  overflow-x: hidden;
}

.main-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: var(--spacing-large) 0;
  background-image: url(/assets/images/s10background.png);
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
  margin: 0 auto;
}

/* --- TITLE STYLING --- */
.title-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 30px;
  margin-top: 20px;
}

.royal-header {
  font-family: 'Cinzel Decorative', serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  line-height: 0.85;
  margin: 0;
  margin-bottom: 5px;
}

.royal-top-row {
  display: flex;
  align-items: center;
  gap: 20px;
}

.eu-icon {
  width: 100px;
  height: 100px;
  color: rgb(37, 150, 190);
  --stroke-color: rgb(17, 73, 94);
  position: relative;
  top: -5px;
}

.royal-text-top {
  font-size: 80px;
  color: #FFFDF5;
  -webkit-text-stroke: 2px #c28888;
  text-shadow: 4px 4px 0px #8f5353;
  letter-spacing: 2px;
}

.smugs-red {
  -webkit-text-stroke: 2px rgb(189, 38, 43);
  text-shadow: 4px 4px 0px rgb(100, 20, 23);
}

.royal-bottom {
  font-size: 110px;
  color: #FFFDF5;
  -webkit-text-stroke: 3px #c28888;
  text-shadow: 5px 5px 0px #8f5353;
  letter-spacing: -2px;
}

.season-img {
  width: 600px;
  max-width: 90%;
  height: auto;
  filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.2));
  margin-top: 20px;
}

/* --- LEADERBOARD GRID --- */
.leaderboard-container {
  display: grid;
  /* Desktop Layout */
  grid-template-columns: 1fr minmax(1000px, auto) 1fr;
  gap: var(--spacing-large);
  align-items: flex-start;
}

.leaderboard {
  grid-column: 2;
  width: 100%;
}

/* --- PICK'EM GRID --- */
.pickem-container {

}

.pickem {
    width: 100%;
}

/*
   Media Query for mobile devices
   (Screens smaller than 1024px)
*/
@media (max-width: 1024px) {
  .leaderboard-container {
    /* Switch to a single column layout */
    grid-template-columns: 1fr;
    /* Side Padding */
    padding: 0 15px;
  }

  .leaderboard {
    /* Ensure it takes up the full single column */
    grid-column: 1;
  }

  .main-container {
      background-attachment: scroll;
  }
}

/* Responsive Font Sizing */
@media (max-width: 768px) {
    .royal-text-top { font-size: 40px; -webkit-text-stroke: 1px #c28888; text-shadow: 2px 2px 0px #8f5353;}
    .smugs-red { -webkit-text-stroke: 1px rgb(189, 38, 43); text-shadow: 2px 2px 0px rgb(100, 20, 23); }
    .eu-icon { width: 50px; height: 50px; }
    .royal-bottom { font-size: 60px; -webkit-text-stroke: 1.5px #c28888; text-shadow: 3px 3px 0px #8f5353;}
    .season-img { width: 100%; margin-top: 10px;}
}
</style>
