<script>
export default {
    name: "Leaderboard",
    components: {
    },
    props: {
        players: {
            type: Array,
            required: true,
        },
    },
    data() {
        return {
            // Copy of dictionary for frontend mapping
            characterMap: {
                1: "Jackie Mini", 2: "Aya Mini", 3: "Fiora Mini", 4: "Magnus Mini", 5: "Zahir Mini",
                6: "Nadine Mini", 7: "Hyunwoo Mini", 8: "Hart Mini", 9: "Isol Mini", 10: "Li Dailin Mini",
                11: "Yuki Mini", 12: "Hyejin Mini", 13: "Xiukai Mini", 14: "Chiara Mini", 15: "Sissela Mini",
                16: "Silvia Mini", 17: "Adriana Mini", 18: "Shoichi Mini", 19: "Emma Mini", 20: "Lenox Mini",
                21: "Rozzi Mini", 22: "Luke Mini", 23: "Cathy Mini", 24: "Adela Mini", 25: "Bernice Mini",
                26: "Barbara Mini", 27: "Alex Mini", 28: "Sua Mini", 29: "Leon Mini", 30: "Eleven Mini",
                31: "Rio Mini", 32: "William Mini", 33: "Nicky Mini", 34: "Nathapon Mini", 35: "Jan Mini",
                36: "Eva Mini", 37: "Daniel Mini", 38: "Jenny Mini", 39: "Camilo Mini", 40: "Chloe Mini",
                41: "Johann Mini", 42: "Bianca Mini", 43: "Celine Mini", 44: "Echion Mini", 45: "Mai Mini",
                46: "Aiden Mini", 47: "Laura Mini", 48: "Tia Mini", 49: "Felix Mini", 50: "Elena Mini",
                51: "Priya Mini", 52: "Adina Mini", 53: "Markus Mini", 54: "Karla Mini", 55: "Estelle Mini",
                56: "Piolo Mini", 57: "Martina Mini", 58: "Haze Mini", 59: "Isaac Mini", 60: "Tazia Mini",
                61: "Irem Mini", 62: "Theodore Mini", 63: "Ly Anh Mini", 64: "Vanya Mini", 65: "Debi & Marlene Mini",
                66: "Arda Mini", 67: "Abigail Mini", 68: "Alonso Mini", 69: "Leni Mini", 70: "Tsubame Mini",
                71: "Kenneth Mini", 72: "Katja Mini", 73: "Charlotte Mini", 74: "Darko Mini", 75: "Lenore Mini",
                76: "Garnet Mini", 77: "Yumin Mini", 78: "Hisui Mini", 79: "Justyna Mini", 80: "István Mini",
                81: "NiaH Mini", 82: "Xuelin Mini", 83: "Henry Mini", 84: "Blair Mini", 85: "Mirka Mini",
            }
        };
    },
    watch: {
    },
    computed: {
        sortedPlayers() {
            const active = this.players
                .filter(p => !p.is_eliminated)
                .sort((a, b) => b.mmr - a.mmr);
            const eliminated = this.players
                .filter(p => p.is_eliminated)
                .sort((a, b) => a.eliminated_at_rank - b.eliminated_at_rank);

            return [...active, ...eliminated];
        }
    },
    methods: {
        setRankImage(mmr){
            if (mmr >= 7000) return "Immortal.png";
            if (mmr >= 6400) return "Meteorite.png";
            if (mmr >= 5000) return "Diamond.png";
            if (mmr >= 3600) return "Platinum.png";
            return "Unranked.png";
        },
        placeClass(index){
            if (index == 0) return "firstPlace";
            if (index == 1) return "secondPlace";
            if (index == 2) return "thirdPlace";
            return null;
        },
        top3Characters(player) {
            const list = Array.isArray(player.character_stats) ? player.character_stats : [];
            return [...list]
                .sort((a, b) => (b.totalGames ?? 0) - (a.totalGames ?? 0))
                .slice(0, 3);
        },
        pickRate(cs, player) {
            const total = player?.games ?? 0;
            const g = cs?.totalGames ?? 0;
            return total > 0 ? ((g / total) * 100).toFixed(1) : "0.0";
        },
        getCharIconPath(code) {
            const fileName = this.characterMap[code];
            if (!fileName) return "";
            return new URL(`../assets/images/character_icons/${fileName}.png`, import.meta.url).href;
        }
    },
}
</script>

<template>
  <p>DEBUG Leaderboard mounted</p>

  <div id="leaderboard-inner">
    <div
      v-for="(player, index) in sortedPlayers"
      :key="player.name"
      class="playerCard"
      :class="placeClass(index)"
    >
      <!-- Locked Overlay-->
      <div v-if="player.is_eliminated" class="eliminatedOverlay"></div>

      <p class="rank">{{ index + 1 }}</p>
      <img
        class="playerIcon"
        :src="`/src/assets/images/${player.name}.png`"
        :alt="player.name + 's Icon'"
      />

      <p class="playerMMR">
        <img
          class="rankImage"
          :src="`/src/assets/images/EternalReturnRanks/${setRankImage(player.mmr)}`"
          alt="Rank icon"
        />
        <span class="playerMMRNumber">{{ player.mmr }} RP</span>
      </p>
      <div class="playerNameContainer">
        <p class="playerName">{{ player.name }}</p>
      
        <div v-if="player.twitchStatus" class="twitchLiveStatus">
          <span class="red-dot"></span>
        </div>
      </div>
      <p class="playerGames">
        <span class="stat-label">Games:</span>
        {{ player.games }}
      </p>
      <p class="playerWinRate">
        <span class="stat-label"> Winrate: </span> {{ player.win_rate }}%
      </p>

      <!-- DEBUG: show computed top 3 ids -->
    <!--  <span class="top3Debug"> -->
    <!--    icons={{ player.top_character_icons }} | top3={{ top3Characters(player).map(cs => cs.characterCode) }} -->
    <!--  </span> -->

        <!-- Char 1 -->
      <div class="playerCharacter1">
        <template v-if="top3Characters(player)[0]">
          <img
            class="playerCharacter1-img"
            :src="getCharIconPath(top3Characters(player)[0].characterCode)"
            :alt="characterMap[top3Characters(player)[0].characterCode]"
          />
          <div class="charStat">{{ pickRate(top3Characters(player)[0], player) }}%</div>
        </template>
      </div>

      <!-- Char 2 -->
      <div class="playerCharacter2">
        <template v-if="top3Characters(player)[1]">
          <img
            class="playerCharacter2-img"
            :src="getCharIconPath(top3Characters(player)[1].characterCode)"
            :alt="characterMap[top3Characters(player)[1].characterCode]"
          />
          <div class="charStat">{{ pickRate(top3Characters(player)[1], player) }}%</div>
        </template>
      </div>

      <!-- Char 3 -->
      <div class="playerCharacter3">
        <template v-if="top3Characters(player)[2]">
          <img
            class="playerCharacter3-img"
            :src="getCharIconPath(top3Characters(player)[2].characterCode)"
            :alt="characterMap[top3Characters(player)[2].characterCode]"
          />
          <div class="charStat">{{ pickRate(top3Characters(player)[2], player) }}%</div>
        </template>
      </div>

      

      <!-- Twitch Icon -->
      <a
        class="twitchLink"
        :href="`https://twitch.tv/${player.twitch}`"
        target="_blank"
        rel="noopener noreferrer"
      >
        <i class="fa-brands fa-twitch"></i>
      </a>

      <!-- Dak Icon -->
      <a
        :href="`https://dak.gg/er/players/${player.name}`"
        class="playerDak"
        target="_blank"
        rel="noopener noreferrer"
      >
        <img src="https://cdn.dak.gg/er/images/gnb/dakgg.svg" alt="Dak.gg" class="dakIcon" />
      </a>

    </div>
  </div>
</template>

<style scoped>
.player-card-list {
  display: grid;
  grid-template-columns: 1fr;
}
/*
.top3Debug {*/
/*  grid-column: 7 / 10;   /* spans columns 7-9 */
 /*  justify-self: center;*/
 /* font-size: 10px;*/
 /* opacity: 0.8;*/
/*}*/

.charStat {
  font-size: 11px;
  /* font-weight: bold; */
  /* color: #ffffff; */
  margin-top: 4px;
  /* text-shadow: 1px 1px 2px #000000, 0 0 1em #000000; */
  opacity: 1;
}

.playerCard {
  display: grid;
  grid-template-columns:
    var(--grid-small) /* 1: Rank      */
    var(--grid-large) /* 2: Icon      */
    var(--grid-large) /* 3: MMR       */
    var(--grid-xlarge) /* 4: Name      */
    var(--grid-medium) /* 5: Games     */
    var(--grid-medium) /* 6: Winrate   */
    var(--grid-small) /* 7: Char1     */
    var(--grid-small) /* 8: Char2     */
    var(--grid-small) /* 9: Char3     */
    var(--grid-small) /* 10: Live     */
    var(--grid-medium) /* 11: Twitch   */
    minmax(var(--grid-medium), 1fr); /*dak, twitch, Last column stretches */
  background-color: var(--background-dark-grey);
  align-items: center;
  width: 100%;
  border: var(--border-color) solid 2px;
  border-radius: var(
    --border-radius-medium
  );
  justify-items: left;
  position: relative;
  z-index: 2;
  margin-bottom: 1px; /* To put some space between each playerCard */
}

.firstPlace::before,
.secondPlace::before,
.thirdPlace::before {
  content: "";
  position: absolute;
  top: -2px; /* To put the colored border right on top of the classic one */
  left: -2px; /* To put the colored border right on top of the classic one */
  width: calc(100%);
  height: calc(100%);
  z-index: -1;
  border-radius: var(
    --border-radius-medium
  );
}

.firstPlace::before {
  border: 2px solid gold;
  background-color: rgba(255, 217, 0, 0.2); /* Transparent gold overlay */
}

.secondPlace::before {
  border: 2px solid silver;
  background-color: rgba(192, 192, 192, 0.2); /* Transparent silver overlay */
}

.thirdPlace::before {
  border: 2px solid coral;
  background-color: rgba(255, 127, 80, 0.2); /* Transparent coral overlay */
}

.eliminatedOverlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 4;
  pointer-events: none;
  filter: grayscale(100%);
  border-radius: var(--border-radius-medium);
}

/* Player Card Stats */
.rank {
  font-family: "Signika Negative", sans-serif;
  justify-self: center;
  grid-column: 1;
  font-size: var(--font-size-xxlarge);
}

.playerIcon {
  width: 100px;
  height: 100px;
  grid-column: 2;
}

.playerMMR {
  grid-column: 3;
  padding-left: var(--spacing-medium);
  font-size: medium;
  font-weight: 600;

  display: flex;
  flex-direction: column;
  align-items: center ;
  justify-content: center;
  position: relative;

}

.playerMMRNumber {
  align-self: end;
  position: relative;
  bottom: -13px;
}
.rankImage {
  height: 50px;
  transform: scale(1.6);
  margin-left: -10px;
  margin-right: -10px;
}
.playerName {
  grid-column: 4;
  font-size: var(--font-size-large);
  font-weight: 600;
  align-self: left;
  justify-self: left;
}
.playerGames {
  grid-column: 5;
}
.playerWinRate {
  grid-column: 6;
}

.playerCharacter1,
.playerCharacter2,
.playerCharacter3 {
  justify-self: center;
  margin-left: 0;

  /* Flexbox to stack icons and text vertically */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.twitchLiveStatus {
  grid-column: 10;
  margin-left: auto;
}

/* Container for the Name + Dot */
.playerNameContainer {
  grid-column: 4; /* Occupies the name column */
  display: flex;
  align-items: center;
  gap: 8px; /* Space between name and dot */
}

.twitchLiveStatus {
  display: flex;
  align-items: center;
}

.red-dot {
  height: 10px;
  width: 10px;
  background-color: #ff0000;
  border-radius: 50%;
  box-shadow: 0 0 5px #ff0000;
  animation: pulse-red 2s infinite;
  flex-shrink: 0; /* Prevents the dot from squishing if the name is long */
}

.playerName {
  font-size: var(--font-size-large);
  font-weight: 600;
  white-space: nowrap;
}

@keyframes pulse-red {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 0, 0, 0.7); }
  70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(255, 0, 0, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 0, 0, 0); }
}

.playerCharacter1,
.playerCharacter2,
.playerCharacter3 {
  justify-self: center;
  align-self: self-end;
  font-size: smaller;
}

.playerCharacter1-img,
.playerCharacter2-img,
.playerCharacter3-img {
  height: 55px;
  width: auto;
  object-fit: contain;
  filter: drop-shadow(0px 2px 3px rgba(0,0,0,0.3));
}


.stat-label {
  color: var(--font-light-color);
  font-weight: lighter;
}

.twitchLink {
  grid-column: 11;
  justify-self: end;
  padding-right: 6px;
}
.twitchLink:link {
  color: var(--twitch-main-color);
  text-decoration: none;
}

.twitchLink:visited {
  color: var(--twitch-main-color);
  text-decoration: none;
}

.twitchLink:hover {
  color: var(--twitch-secondary-color);
  text-decoration: underline;
}

.playerDak {
  grid-column: 12;
  padding-left: var(--spacing-xsmall);
  text-decoration: none;
  color: var(--white-color);
}

.playerDak:visited {
  color: var(--white-color);
  text-decoration: none;
}

.playerDak:hover {
  filter: brightness(0) saturate(100%) invert(70%);
}

p {
  margin: 0;
}
</style>
