<script>
import draggable from 'vuedraggable';
import PickEmCard from "./PickEmCard.vue"

export default {
    name: "PickEm",
    components: {
        draggable,
        PickEmCard
    },
    data() {
        return {
            // TODO Make this retreived by the API
            playersToPick: [{
                name: "Lesys",
                mmr: 6500,
                games: 50,
                win_rate: 12,
                character_stats: null,
                twitch: "lesys",
                twitchStatus: false,
                is_eliminated: false,
                eliminated_at_rank: null,
            }, {
                name: "Smugdragon",
                mmr: 8000,
                games: 200,
                win_rate: 14,
                character_stats: null,
                twitch: "smugdragoner",
                twitchStatus: false,
                is_eliminated: true,
                eliminated_at_rank: null,
            }, {
                name: "Baumi",
                mmr: 8000,
                games: 200,
                win_rate: 14,
                character_stats: null,
                twitch: "smugdragoner",
                twitchStatus: false,
                is_eliminated: true,
                eliminated_at_rank: null,
            }, {
                name: "FDGood",
                mmr: 8000,
                games: 200,
                win_rate: 14,
                character_stats: null,
                twitch: "smugdragoner",
                twitchStatus: false,
                is_eliminated: true,
                eliminated_at_rank: null,
            }, {
                name: "Leitnessen",
                mmr: 8000,
                games: 200,
                win_rate: 14,
                character_stats: null,
                twitch: "smugdragoner",
                twitchStatus: false,
                is_eliminated: false,
                eliminated_at_rank: null,
            }, {
                name: "Patrei",
                mmr: 8000,
                games: 200,
                win_rate: 14,
                character_stats: null,
                twitch: "smugdragoner",
                twitchStatus: false,
                is_eliminated: false,
                eliminated_at_rank: null,
            }],
            // TODO If a player already has made his choice ans saved, initialize with the saved arrays
            playersTop: [],
            playersEliminatedOrder: [],
        };
    },
    computed: {


    },
    methods: {

    }
}
</script>

<template>

    <div class="container">
        <div class="row">
            <div class="left-side">
                <h3>Pick the players !</h3>
                <div class="player-container">
                    <draggable
                        v-model="playersToPick"
                        item-key="name"
                        group="players"
                        class="draggableContainer"
                    >
                        <template #item="{element}">
                            <PickEmCard :playerName="element.name"></PickEmCard>
                        </template>

                    </draggable>
                </div>
            </div>
            <div class="right-side">
                <h3>Top players</h3>
                <div class="player-container">
                    <div class="top-player-container">
                        <div class="topPlayers">
                            <h3>Top 1</h3>
                            <draggable
                                v-model="playersTop"
                                item-key="name"
                                group="players"
                                class="draggableContainer"
                            >
                                <template #item="{element}">
                                    <PickEmCard :playerName="element.name"></PickEmCard>
                                </template>

                            </draggable>
                        </div>
                        <div class="topPlayers">
                            <h3>Top 2</h3>
                            <draggable
                                v-model="playersEliminatedOrder"
                                item-key="name"
                                group="players"
                                class="draggableContainer"
                            >
                                <template #item="{element}">
                                    <PickEmCard :playerName="element.name"></PickEmCard>
                                </template>

                            </draggable>
                        </div>
                        <div class="topPlayers">
                            <h3>Top 3</h3>
                            <draggable
                                v-model="playersEliminatedOrder"
                                item-key="name"
                                group="players"
                                class="draggableContainer"
                            >
                                <template #item="{element}">
                                    <PickEmCard :playerName="element.name"></PickEmCard>
                                </template>

                            </draggable>
                        </div>
                    </div>
                </div>
                <h3>Order of eliminations</h3>
                <div class="player-container">
                    <draggable
                        v-model="playersEliminatedOrder"
                        item-key="name"
                        group="players"
                        class="draggableContainer"
                    >
                        <template #item="{element}">
                            <PickEmCard :playerName="element.name"></PickEmCard>
                        </template>

                    </draggable>
                </div>

            </div>
        </div>
    </div>

</template>

<style>

.playerIcon {
    width: 100px;
    height: 100px;
    grid-column: 2;
}

.container {
    padding-right:15px;
    padding-left:15px;
    margin-right:auto;
    margin-left:auto;
    width: 100%;
    display: flex;
    align-items: center;
}

.topPlayers {
    width: 30%;
    margin-left: 1%;
    margin-right: 1%;
}

.row {
    display: flex;
    align-items: center;
    width: 100%;
    height: 100%;
}

.container::after,
.row:after,
.row:before {
    width: 100%;
    height: 100%;
}
.row:after {
    clear:both;
}

.left-side,
.right-side {
    width: 45%;
    margin: 2%;
}

.player-container {
    height: auto;
    min-height: 100px;
    border: solid 2px black;
    width: 100%;
}

.top-player-container {
    display: block ruby;
    align-items: center;
    padding-left: 2% !important;
    padding-right: 2% !important;
    text-align: center;
}

.draggableContainer {
    height: auto;
    min-height: 100px;
}
</style>
