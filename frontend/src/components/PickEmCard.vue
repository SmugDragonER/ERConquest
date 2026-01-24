<script>

export default {
    name: "PickEmCard",
    components: {
    },
    props: {
        playerName: null
    },
    data() {
        return {
        };
    },
    computed: {


    },
    methods: {

    }
}
</script>

<template>
    <div class="tooltip iconAndName">
        <img
          class="playerIcon"
          :src="`/src/assets/images/${playerName}.png`"
          :alt="playerName + 's Icon'"
        />
        <span class="tooltiptext">{{ playerName }}</span>
    </div>

</template>

<style>

.playerIcon {
    width: 100px;
    height: 100px;
}

.iconAndName {
    vertical-align: top;
    display: inline-block;
    text-align: center;
    width: 100px;
    height: 100px;
}

/* Tooltip container */
.tooltip {
  position: relative;
  display: inline-block;
  border-bottom: 1px dotted black; /* Add dots under the hoverable text */
  cursor: pointer;
}

/* Tooltip text */
.tooltiptext {
  visibility: hidden; /* Hidden by default */
  width: auto;
  background-color: black;
  color: #ffffff;
  text-align: center;
  padding: 5px 5px;
  border-radius: 6px;
  position: absolute;
  z-index: 99; /* Ensure tooltip is displayed above content */
}

/* Show the tooltip text on hover */
.tooltip:hover .tooltiptext {
  visibility: visible;
}
</style>
