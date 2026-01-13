<script>
import Leaderboard from './Leaderboard.vue';

export default {
    name: "MainContent",
    components: {
        Leaderboard,
    },
    data() {
        return {
            players: [],
            loading: true,
            error: null,
            apiUrl: 'http://127.0.0.1:8000/get_latest_leaderboard',
        };
    },
    watch: {
    },
    computed: {
    },
    methods: {
    },
    async mounted() {
        this.loading = true
        this.error = null

        try {
            const response = await fetch(this.apiUrl)
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.status)
            }

            const data = await response.json()
            this.players = Object.values(data.entries).map(player => ({
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
            this.error = e.message
        } finally {
            this.loading = false
        }
    }
}
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
