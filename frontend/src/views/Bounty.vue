<template>
  <div class="bounty-board">
    <h1 class="board-title">Active Bounties</h1>
    
    <div class="bounty-grid">
      <!-- Beispiel Bounty -->

      <div class="bounty-card">
        <div class="bounty-header">
          <h3 class="bounty-title">🐟 Sacrifice to the sea god 🐟
            <span class="bounty-reward">10€</span>
          </h3>
        </div>
        <div class="bounty-body">
          <p class="bounty-desc">Place a ritual circle of at least 6 raw/cooked fish 🐟 in a ring on the ground. If an enemy test subject then dies within the circle, the tribute is complete and you win the bounty. 
            <br/><br/>
            (You can make it easier by making the circle bigger if you add more fish. Just be reasonable, it doesnt count as a circle if you place one in each corner of the map.)
          </p>
          <div class="bounty-poster">
            <span class="posted-by">Posted by: </span>
            <strong>FishyFishy 🐟</strong>
          </div>
        </div>
      </div>


      <div class="bounty-card">
        <div class="bounty-header">
          <h3 class="bounty-title">360 noscope
            <span class="bounty-reward">10€</span>
          </h3>
        </div>
        <div class="bounty-body">
          <p class="bounty-desc">Spin around for at least 360 degrees, then land the final blow on an enemy test subject with sniper skill (D)
                                <br/><br/>(Doesnt count if they give up and stand still)
          </p>
          <div class="bounty-poster">
            <span class="posted-by">Posted by: </span>
            <strong>FishyFishy 🐟</strong>
          </div>
        </div>
      </div>

      <div class="bounty-card">
        <div class="bounty-header">
          <h3 class="bounty-title">Most Viewed Clip
            <span class="bounty-reward">25€</span>
          </h3>
        </div>
        <div class="bounty-body">
          <p class="bounty-desc"> Twitch Clip with the most Views!
                                <br/><br/>
                                (Must be posted into the Conquest discord, can also be posted by viewers!)
          </p>
          <div class="bounty-poster">
            <span class="posted-by">Posted by: </span>
            <strong>SmugDragon</strong>
          </div>
        </div>
      </div>


    </div>
  </div>
</template>

<script>
export default {
  name: "Bounty"
}
</script>

<style scoped>
    
  /* Bounty Board spezifische Styles */
 .bounty-board {
    max-width: 1200px;
    margin: 3rem auto;
    padding: 0 1.5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .board-title {
    color: var(--primary-color);
    text-align: center;
    text-transform: uppercase;
    font-size: 2.5rem;
    margin-bottom: 3rem;
    width: 100%;
    text-shadow: 0px 0px 30px rgba(0, 0, 0);
  }

  .bounty-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    justify-content: center; 
    gap: 2rem;
    width: 100%;
    max-width: 100%;
    margin: 0;
  }

 .bounty-card {
    background-color: #1a1d26; /* Dark background */
    border: 2px solid var(--primary-color);
    border-radius: 16px;
    display: flex;
    flex-direction: column;
    transition: all 0.3s ease;
    overflow: hidden;
  }

  .bounty-header {
    padding-top: 1.5rem;
    padding-bottom: 0.5rem;
    display: flex;
    justify-content: center;
    align-items: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  }

  .bounty-title {
    color: #fff;
    font-size: 1.5rem;
    font-weight: 700;
    align-self: center;
    margin: 0;
  }

  .bounty-reward {
    color: var(--primary-color);
    font-size: 1.3rem;
    font-weight: 800;
    padding: 0.2rem 0.5rem;
    background: rgba(var(--primary-color-rgb), 0.1); /* Falls RGB-Variable existiert */
    border: 1.5px solid var(--primary-color);
    border-radius: 30px; 
  }

  .bounty-body {
    padding: 1.5rem;
    padding-top: 1.2rem;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
  }

  .bounty-desc {
    color: white;
    line-height: 1.6;
    margin-bottom: 2rem;
    flex-grow: 1;
  }

  .bounty-footer {
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 1rem;
    font-size: 0.85rem;
    display: flex;
    justify-content: space-between;
    color: #666;
  }

  .bounty-footer strong {
    color: var(--primary-color);
  }
  .posted-by {
    color: #a0a0a0;
  }

  @media (max-width: 768px) {
    .bounty-grid {
      grid-template-columns: 1fr;
    }
  }

</style>