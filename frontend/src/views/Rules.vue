<template>
  <div class="rules-page">
    <h1 id="event-information">Event Information</h1>

    <div class="rule-container">
      <span class="RuleWord">Rules</span>
      <ul class="rules-list">
        <li>60% of Games must be streamed</li>
        <li>All Games must be played on the EU server</li>
        <li>General Fair Play rules</li>
      </ul>
    </div>

    <div class="rule-container" id="elimination-container">
      <span class="RuleWord">Eliminations</span>
      <p class="rules-subtitle">Eliminations happen at <strong>3 AM CET</strong></p>
      
      <div class="elim-grid">
        <div class="grid-row"><span>29.01 - 01.02:</span> <strong>0 Elims</strong></div>
        <div class="grid-row"><span>02.02:</span>         <strong>5 Elims</strong></div>
        <div class="grid-row"><span>03.02:</span>         <strong>4 Elims</strong></div>
        <div class="grid-row"><span>04.02:</span>         <strong>3 Elims</strong></div>
        <div class="grid-row"><span>05.02 - 06.02:</span> <strong>2 Elims</strong></div>
        <div class="grid-row"><span>07.02 - 10.02:</span> <strong>1 Elim</strong></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
    .rule-container {
        background-color: #1a1d26; 
        padding: 1.5rem;
        border: 1px solid var(--border-color);
        border-radius: 8px; 
        margin-bottom: 2rem;
    }

    .RuleWord {
        color: var(--primary-color);
        font-size: 1.4rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 1rem;
        display: block;
    }
    .rules-list {
        list-style: none;
        padding: 0;
        color: var(--accent-color);
        text-align: left;
        display: inline-block; 
    }

    .rules-list li {
        margin-bottom: 0.5rem;
        position: relative;
        padding-left: 1.5rem;
    }

    .rules-list li::before {
        content: "•";
        color: var(--primary-color);
        position: absolute;
        left: 0;
    }

    .elim-grid {
        max-width: 350px;
        margin: 0 auto;
    }

    .grid-row {
        display: flex;
        justify-content: space-between;
        padding: 0.5rem 1rem;
        border-radius: 4px;
    }

    .grid-row:nth-child(odd) {
        background-color: rgba(255, 255, 255, 0.03);
    }

    .grid-row strong {
        color: var(--primary-color);
    }
    
  h1 {
    color: var(--primary-color);
    font-weight: bolder;
    margin-bottom: 2rem;
    text-align: center;
  }
</style>