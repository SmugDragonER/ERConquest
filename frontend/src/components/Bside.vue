<script></script>

<template>
    <div id="leaderboard-right" class="leaderboard-right">
        <p class="Rules"><span class="RuleWord">Rules:</span>- 90% of Games must be streamed<br>- All Games must be played on the EU server<br>- General Fair Play rules</p>
        <p class="Rules"><span class="RuleWord">Eliminations:</span>
            - First 3 Days:&nbsp;No Elims <br>
            - After Day 3:&nbsp;&nbsp;3 Elims Daily <br>
            - TOP 3:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 Elims Daily <br>
            - Elims happen after ranked
        </p>
    </div>
</template>

<style>
        .leaderboard-right{
        padding-left: var(--spacing-xlarge);
        grid-column: 3;
        display: flex;
        flex-direction: column;
        align-items: start;
        text-align: start;
    }
    
    .Rules{
            background-color: var(--background-dark-grey);
            padding: var(--spacing-small);
            border: var(--border-color) solid 1px;
            display: block;
            justify-content: center;
            align-items: center;
            color: var(--accent-color);
        }

        .RuleWord{
            color: var(--primary-color);
            display: flex;
            justify-content: start;
            padding-left: 3%;
        }

</style>