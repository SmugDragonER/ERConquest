<script>
</script>

<template>
  <div class="rules-page">
    <h1>Event Information</h1>

    <div class="rule-container">
      <p class="Rules">
        <span class="RuleWord">
        Rules
        </span>
        - 60% of Games must be streamed
        <br/>
        - All Games must be played on the EU server
        <br/>
        - General Fair Play rules
      </p>

    </div>
    <div class="rule-container">
      <p class="Rules">
        <span class="RuleWord">
          Eliminations:
        </span>
        - Day 1-3: No Eliminations
        <br/>
        - Day 3-x: Y Elimination
      </p>
    </div>
  </div>

</template>

<style scoped>
    .rules-page {
        background-color:var(--background-dark-grey);
        color: var(--primary-color);
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem;
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
        font-size: large;
        justify-content: center;
        padding-bottom: 0.5rem;
    }
</style>
