document.addEventListener("DOMContentLoaded", function () {
    const contactButton = document.getElementById("contact-button");
    const contactBox = document.getElementById("contact-box");

    const lastUpdatedElement = document.getElementById("last-updated");

    contactButton.addEventListener("click", () => {
        contactBox.style.display = (contactBox.style.display === "block") ? "none" : "block";
    });

    // Hide the box when clicking outside of it
    document.addEventListener("click", (event) => {
        if (!contactBox.contains(event.target) && event.target !== contactButton) {
            contactBox.style.display = "none";
        }
    });

        // Fetch and display the last updated time
        fetch('data/last_updated.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch last updated time: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            lastUpdatedElement.textContent = `${data}`;
        })
        .catch(error => {
            console.error('Error fetching last updated time: Contact Smug', error);
            lastUpdatedElement.textContent = 'Error fetching last updated time';
        });

    // Fetch both leaderboard_data.json and player_IDs.json
    Promise.all([
        fetch('data/leaderboard_data.json').then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        }),
        fetch('data/player_ID.json').then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
    ])
    .then(([leaderboardData, playerIDs]) => {
        const leaderboard = document.getElementById('leaderboard');
        const players = leaderboardData.players;

        players.forEach((player, index) => {
            const playerCard = document.createElement('div');
            playerCard.classList.add('playerCard');

            switch (index) {
                case 0:
                    playerCard.classList.add('firstPlace');
                    break;
                case 1:
                    playerCard.classList.add('secondPlace');
                    break;
                case 2:
                    playerCard.classList.add('thirdPlace');
                    break;
            };

            const isLocked = playerIDs[player.playerName]?.locked;
            console.log(`Player: ${player.playerName}, Locked: ${isLocked}`); // Debugging

            let rankImage;
            switch (true) {
                case (player.playerMMR >= 7000):
                    rankImage = "Immortal.png";
                    break;
                case (player.playerMMR >= 6400):
                    rankImage = "Meteorite.png";
                    break;
                case (player.playerMMR >= 5000):
                    rankImage = "Diamond.png";
                    break;
                case (player.playerMMR >= 3600):
                    rankImage = "Platinum.png";
                    break;
                default:
                    rankImage = "Unranked.png";
            }

            playerCard.innerHTML = `
                <p class="rank">${index + 1}</p>
                <img class="playerIcon" src="images/${player.playerName}.png" alt="${player.playerName}s Icon">
                <p class="playerMMR"><img src="images/${rankImage}" class="rankImage"><br><span class="playerMMRNumber">${player.playerMMR} RP</span></p>
                <p class="playerName">${player.playerName}</p>
                <p class="playerWinRate"><span class="stat-label">Winrate:<br></span> ${player.playerWinRate}%</p>
                <p class="playerGames"><span class="stat-label">Games:<br></span> ${player.playerGames}</p>
                ${player.playerCharacterStats && Array.isArray(player.playerCharacterStats) ?`
                    ${player.playerCharacterStats[0] ? `
                    <p class="playerCharacter1"><img src="images/character_icons/${player.playerCharacterStats[0].playerCharacterCode}.png" class="playerCharacter1-img"><br>${player.playerCharacterStats[0].playerCharacterPickRate}%
                    </p>`:""}
                    
                    ${player.playerCharacterStats[1] ? `
                    <p class="playerCharacter2"><img src="images/character_icons/${player.playerCharacterStats[1].playerCharacterCode}.png" class="playerCharacter2-img"><br>${player.playerCharacterStats[1].playerCharacterPickRate}% 
                    </p>` : ""}
                    
                    ${player.playerCharacterStats[2] ? `
                    <p class="playerCharacter3"><img src="images/character_icons/${player.playerCharacterStats[2].playerCharacterCode}.png" class="playerCharacter3-img"><br>${player.playerCharacterStats[2].playerCharacterPickRate}% 
                    </p>` : ""}
                `: ""}
                <a href="https://twitch.tv/${player.playerTwitch}" class="twitchLink">
                    <i class="fa-brands fa-twitch"></i>
                </a>
                <a href="https://dak.gg/er/players/${player.playerName}" class="playerDak">
                    <p class="playerDak">Dak.gg</p>
                </a>
            `;
            leaderboard.appendChild(playerCard);
        });

        // Add overlays after rendering all player cards
        players.forEach((player, index) => {
            const isLocked = playerIDs[player.playerName]?.locked;
            const playerCard = leaderboard.children[index];

            if (isLocked) {
                const lockedOverlay = document.createElement('div');
                lockedOverlay.classList.add('lockedOverlay');
                playerCard.appendChild(lockedOverlay);
                console.log(`Locked overlay added for ${player.playerName}`);
            }

        });
    })
    .catch(error => console.error('Error with getting data:', error));
});