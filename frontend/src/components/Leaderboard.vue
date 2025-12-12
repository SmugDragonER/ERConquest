<script setup>
import { ref, onMounted } from 'vue'

const players = ref([])
const playerIDs = ref({})
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const [lbRes, idRes] = await Promise.all([
      fetch('http://127.0.0.1:8000/build_leaderboard'),
      fetch('http://127.0.0.1:8000/player_ids_endpoint') // später anpassen
    ])
    // JSON parsen und players / playerIDs entsprechend deinem neuen Format setzen
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
})
</script>

<template>
    <div id="leaderboard">
        <div
            v-for="(player, index) in players"
            :key="player.name"
            class="playerCard"
            :class="placeClass(index)"
        >
            <!-- Name, MMR, Wirate etc. als {{ }}-->
        </div>
    </div>

</template>

<!-- hilfsfunktionen oder computed properties statt switch + create element-->
 