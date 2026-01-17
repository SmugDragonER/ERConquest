<script>
</script>

<template>
  <div class="rules-page">
    <h1>Rules</h1>

    <div class="rule-container">
      <p class="Rules">
        <span class="RuleWord">
          Rules:
        </span>
        - 90% of Games must be streamed
        <br/>
        - All Games must be played on the EU server
        <br/>
        - General Fair Play rules
      </p>

    </div>
    <div class="rule-container">
      <p class="Rules">
        <span class="RuleWord">
          How do Eliminations work?
        </span>
        - First 3 Days: No Eliminations
        <br/>
        - After Day 3:
      </p>
    </div>
  </div>

</template>

<style scoped>
    .rules-page {
        color: white;
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
        justify-content: start;
        padding-left: 3%;
    }
</style>
