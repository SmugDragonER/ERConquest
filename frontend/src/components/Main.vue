<script>
    import Leaderboard from './Leaderboard.vue'
</script>

<template>
    <main class="main-container">
        <div class="content-container">
            <div id="title" class="title">
                <h1><img src="./assets/images/Smugs-Conquest-Title.png" alt="title" class="titleimg"></h1>
            </div>
            <div class="leaderboard-container">
                <div id="leaderboard-left" class="leaderboard-left"></div>
                <div id="leaderboard" class="leaderboard"></div>
                <div id="leaderboard-right" class="leaderboard-right">
                    <p class="Rules"><span class="RuleWord">Rules:</span>- 90% of Games must be streamed<br>- All Games must be played on the EU server<br>- General Fair Play rules</p>
                    <p class="Rules"><span class="RuleWord">Eliminations:</span>
                        - First 3 Days:&nbsp;No Elims <br>
                        - After Day 3:&nbsp;&nbsp;3 Elims Daily <br>
                        - TOP 3:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 Elims Daily <br>
                        - Elims happen after ranked
                    </p>
                </div>
            </div>
        </div>
    </main>

</template>

<style></style>