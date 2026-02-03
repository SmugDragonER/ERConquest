<script>
import { RouterLink } from 'vue-router';
import Bounty from '../views/Bounty.vue';
import Rules from '../views/Rules.vue';

export default {
    name: "Header",
    components: { Rules, /*Bounty*/ },
    data() {
        return {
            isOpenContact: false,
            isOpenRules: false,
            //isOpenBounty: false,
        };
    },
    watch: {
        isOpenContact(val) { this.handleListener(val); },
        isOpenRules(val) { this.handleListener(val); },
        //isOpenBounty(val) { this.handleListener(val); },
    },
    methods: {
        handleListener(val) {
            if (val) {
                setTimeout(() => document.addEventListener("click", this.handleClickOutside), 0);
            } else if (!this.isOpenContact && !this.isOpenRules) {
                document.removeEventListener("click", this.handleClickOutside);
            }
        },
        toggleBox(elementToToggle) {
            this["isOpen" + elementToToggle] = !this["isOpen" + elementToToggle];
        },
        closeBox(elementToClose) {
            this["isOpen" + elementToClose] = false;
        },
        handleClickOutside(event) {
            const contactBox = document.getElementById("contact-box");
            const contactBtn = document.getElementById("contact-button");
            const rulesBox = document.getElementById("rules-box");
            const rulesBtn = document.getElementById("rules-button");
           // const bountyBox = document.getElementById("bounty-box");
           // const bountyBtn = document.getElementById("bounty-button");

            if (contactBox && !contactBox.contains(event.target) && event.target !== contactBtn) {
                this.closeBox("Contact");
            }
            if (rulesBox && !rulesBox.contains(event.target) && event.target !== rulesBtn) {
                this.closeBox("Rules");
            }
            // if (bountyBox && !bountyBox.contains(event.target) && event.target !== bountyBtn) {
            //     this.closeBox("Bounty");
            // }
        }
    },
    beforeUnmount() {
        document.removeEventListener("click", this.handleClickOutside);
    }
}
</script>

<template>

    <header class="main-header">
        <div class="nav-container">
            
            <div class="left-nav-group">
           
                <!-- Drop Down Rules -->

                <div class="popup-wrapper">
                    <span @click.stop="toggleBox('Rules')" id="rules-button" class="nav-link">Event Information</span>
                    <div v-if="isOpenRules" id="rules-box" class="dropdown-box rules-wide">
                        <Rules/>
                    </div>
                </div>

                <router-link
                    v-if="$route.path === '/'"
                    to="/bounty"
                    class="nav-link"
                    id="bounty-button"
                >
                    Bounty Board
                </router-link>

                <router-link
                    v-if="$route.path === '/bounty'"
                    to="/"
                    class="nav-link"
                >
                    Leaderboard
                </router-link>
            </div>
<!--
            <div class="left-header">
                <nav class="header-nav">-->
                    <!-- Show Pick'Em link only on the leaderboard page -->
                    <!--<router-link
                        v-if="$route.path === '/'"
                        to="/pickEm"
                        class="nav-item"
                    >
                        Pick'em
                    </router-link>-->

                    <!-- Show LEADERBOARD link only on the Pick'Em page -->
<!--                    <router-link
                        v-if="$route.path === '/pickEm'"
                        to="/"
                        class="nav-item"
                    >
                        Leaderboard
                    </router-link>
                </nav>
            </div>
            -->

            <div class="popup-wrapper">
                <span @click.stop="toggleBox('Contact')" id="contact-button" class="nav-link">Contact</span>
                <div v-if="isOpenContact" id="contact-box" class="dropdown-box">
                    <p class="title">In case of Issues:</p>
                    <p class="info">Discord: <strong>SmugDragonER</strong></p>
                </div>
            </div>
        </div>
    </header>
</template>

<style scoped>
    .main-header {
        background: var(--background-dark-grey);
        padding: 10px 20px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        display: flex;
        width: auto;
        justify-content: space-between;
    }

    .nav-container {
        display: flex;
        justify-content: space-between;
        width: 100%;
    }

    .nav-link,
    .nav-link:visited,
    .nav-link:active {
        color: var(--primary-color);
        font-weight: bold;
        cursor: pointer;
        transition: color 0.2s;
        justify-content: space-between;
        width: auto;
        text-decoration: none;
    }

    .left-nav-group{
        display: flex;
        gap: 20px;
        align-items: center;
    }
    .left-nav-group > .popup-wrapper::after {
        content: "|";
        color: var(--primary-color);
        margin-left: 20px;
        font-weight: bold;
        pointer-events: none;
    }

    .nav-link:hover { color: #ad936e; }

    .popup-wrapper { position: relative; color: var(--primary-color) }

    .header-left {
        left: 0;
    }

    .dropdown-box {
        position: absolute;
        top: 150%; /* Opens Down */
        right: 0;
        background: #2a2a2a;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #444;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
        z-index: 1000;
        width: 220px;
        color: white;
    }

    .rules-wide {
        width: 400px;
        left: 0;
    }

    /* Downward Arrow */
    .dropdown-box::after {
        content: "";
        position: absolute;
        bottom: 100%;
        right: 15px;
        border-width: 6px;
        border-style: solid;
        border-color: transparent transparent #2a2a2a transparent;
    }

    .rules-wide::after {
        left: 15px; /* Aligns arrow with the button kinda */
        right: auto !important;
    }

    .title { font-size: 12px; margin-bottom: 5px; opacity: 0.8; }
    .info { color: #ad936e; font-size: 14px; }



</style>
