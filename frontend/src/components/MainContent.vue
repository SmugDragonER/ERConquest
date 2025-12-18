<script setup>
import { ref, onMounted } from 'vue';
import Leaderboard from './Leaderboard.vue';

    const players = ref([]);
    const loading = ref(true);
    const error = ref(null);

    const apiUrl = 'http://127.0.0.1:8000/get_latest_leaderboard'


    onMounted(async () => {
        loading.value = true
        error.value = null

        try{
            const response = await fetch(apiUrl)
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.status)
            }

            const data = await response.json()
            players.value = Object.values(data.entries).map(player => ({
                name: player.name,
                mmr: player.mmr,
                games: player.games,
                win_rate: player.win_rate,
                character_stats: player.character_stats,
                twitch: player.twitch,
                twitchStatus: player.is_live_on_twitch,
                is_eliminated: player.is_eliminated,
                eliminated_at_rank: player.eliminated_at_rank,
            }))
        } catch (e) {
            console.error('Error:', e)
            error.value = e.message
        } finally {
            loading.value = false
        }
    })

</script>

<template>
    <div class="leaderboard-wrapper">
        <p v-if="loading">Loading...</p>
        <p v-else-if="error">Error: {{ error }}</p>
        <Leaderboard v-else :players="players" />
    </div>
</template>

<style scoped>
    .leaderboard-wrapper {
        width: 100%;
    }
</style>
