<script setup>
import { computed } from "vue";
const props = defineProps({
  players: {
    type: Array,
    required: true,
  },
});
const sortedPlayers = computed(() => {
  const active = props.players
    .filter((p) => !p.is_eliminated)
    .sort((a, b) => b.mmr - a.mmr);
  const eliminated = props.players
    .filter((p) => p.is_eliminated)
    .sort((a, b) => a.eliminated_at_rank - b.eliminated_at_rank);

  return [...active, ...eliminated];
});

function setRankImage(mmr) {
  let rankImage;
  switch (true) {
    case mmr >= 7000:
      rankImage = "Immortal.png";
      break;
    case mmr >= 6400:
      rankImage = "Meteorite.png";
      break;
    case mmr >= 5000:
      rankImage = "Diamond.png";
      break;
    case mmr >= 3600:
      rankImage = "Platinum.png";
      break;
    default:
      rankImage = "Unranked.png";
  }
  return rankImage;
}

function placeClass(index) {
  let podium = null;
  switch (true) {
    case index == 0:
      podium = "firstPlace";
      break;
    case index == 1:
      podium = "secondPlace";
      break;
    case index == 2:
      podium = "thirdPlace";
      break;
  }
  return podium;
}

// Returns [charId1, charId2, charId3] based on highest totalGames
function top3Characters(player) {
  const list = Array.isArray(player.character_stats) ? player.character_stats : [];
  return [...list]
    .sort((a, b) => (b.totalGames ?? 0) - (a.totalGames ?? 0))
    .slice(0, 3);
}

function characterId(cs) {
  return cs?.characterId ?? cs?.characterCode;
}

function pickRate(cs, player) {
  const total = player?.games ?? 0;
  const g = cs?.totalGames ?? 0;
  return total > 0 ? ((g / total) * 100).toFixed(1) : "0.0";
}

function characterIconPath(characterId) {
  return `/src/assets/images/character_icons/${characterId}.png`;
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
          :src="`/src/assets/ranks/${setRankImage(player.mmr)}`"
          alt="Rank icon"
        />
        <span class="playerMMRNumber">{{ player.mmr }} RP</span>
      </p>
      <p class="playerName">{{ player.name }}</p>
      <p class="playerGames">
        <span class="stat-label">Games:</span>
        {{ player.games }}
      </p>
      <p class="playerWinRate">
        <span class="stat-label"> Winrate: </span> {{ player.win_rate }} %
      </p>

      <!-- DEBUG: show computed top 3 ids -->
<span class="top3Debug">
  icons={{ player.top_character_icons }} | top3={{ top3Characters(player).map(cs => cs.characterCode) }}
</span>

  <!-- Char 1 -->
<div class="playerCharacter1">
  <template v-if="player.top_character_icons?.[0] && top3Characters(player)[0]">
    <img
      class="playerCharacter1-img"
      :src="`/src/assets/images/character_icons/${player.top_character_icons[0]}`"
      alt=""
    />
    <div class="charStat">{{ pickRate(top3Characters(player)[0], player) }}%</div>
  </template>
</div>

<!-- Char 2 -->
<div class="playerCharacter2">
  <template v-if="player.top_character_icons?.[1] && top3Characters(player)[1]">
    <img
      class="playerCharacter2-img"
      :src="`/src/assets/images/character_icons/${player.top_character_icons[1]}`"
      alt=""
    />
    <div class="charStat">{{ pickRate(top3Characters(player)[1], player) }}%</div>
  </template>
</div>

<!-- Char 3 -->
<div class="playerCharacter3">
  <template v-if="player.top_character_icons?.[2] && top3Characters(player)[2]">
    <img
      class="playerCharacter3-img"
      :src="`/src/assets/images/character_icons/${player.top_character_icons[2]}`"
      alt=""
    />
    <div class="charStat">{{ pickRate(top3Characters(player)[2], player) }}%</div>
  </template>
</div>

      <a
        class="twitchLink"
        :href="`https://twitch.tv/${player.twitch}`"
        target="_blank"
      >
        <i class="fa-brands fa-twitch"></i>
      </a>
      <a class="playerDak" :href="`https://dak.gg/er/players/${player.name}`">
        Dak.gg
      </a>
    </div>
  </div>
</template>

<style scoped>
.player-card-list {
  display: grid;
  grid-template-columns: 1fr;
}

.top3Debug {
  grid-column: 7 / 10;   /* spans columns 7-9 */
  justify-self: center;
  font-size: 10px;
  opacity: 0.8;
}

.charStat {
  font-size: 10px;
  text-align: center;
  margin-top: 2px;
  opacity: 0.9;
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
  border: var(--border-color) solid 1px;
  justify-items: left;
  position: relative;
  z-index: 2;
}

.firstPlace::before,
.secondPlace::before,
.thirdPlace::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: calc(100% - 2px); /* Adjust to account for the border width */
  height: calc(100% - 2px); /* Adjust to account for the border width */
  z-index: -1; /* Ensure it stays behind the content */
  border-radius: var(
    --border-radius-medium
  ); /* Match the card's border radius */
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
  align-self: self-end;
  font-size: medium;
  font-weight: 600;
}
.playerMMRNumber {
  align-self: end;
  position: relative;
  bottom: -10px;
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
.playerCharacter1 {
  grid-column: 7;
}
.playerCharacter2 {
  grid-column: 8;
}
.playerCharacter3 {
  grid-column: 9;
}
.twitchLiveStatus {
  grid-column: 10;
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
  height: 60px;
}
.stat-label {
  color: var(--font-light-color);
  font-weight: lighter;
}

.twitchLink {
  grid-column: 11;
  justify-self: end;
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
  color: var(--font-light-color);
}

p {
  margin: 0;
}
</style>
