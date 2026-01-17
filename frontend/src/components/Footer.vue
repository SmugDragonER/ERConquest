<script>
import Rules from '../views/Rules.vue';
export default {
    name: "Footer",
    components: {
        Rules,
    },
    data() {
        return {
            isOpenContact: false, // shows "Contact"- Box
            isOpenRules: false // shows "Contact"- Box
        };
    },
    watch: {
        isOpenContact(val) {
            if (val) {
                setTimeout(() => {
                    document.addEventListener("click", this.handleClickOutside);
                }, 0);
            } else {
                document.removeEventListener("click", this.handleClickOutside);
            }
        },
        isOpenRules(val) {
            if (val) {
                setTimeout(() => {
                    document.addEventListener("click", this.handleClickOutside);
                }, 0);
            } else {
                document.removeEventListener("click", this.handleClickOutside);
            }
        }
    },
    methods: {
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

            if (contactBox && !contactBox.contains(event.target) && event.target !== contactBtn) {
                this.closeBox("Contact");
            }
            // No else to close both if they are both open
            if (rulesBox && !rulesBox.contains(event.target) && event.target !== rulesBtn) {
                this.closeBox("Rules");
            }
        }
    },
}
</script>

<template>
    <footer>
        <!-- Left: Navigation Links -->
        <div class="footer-left">
            <div class="contact-container">
                <span @click.stop="toggleBox('Rules')" id="rules-button" class="footer-link">
                    Rules
                </span>

                <!-- Popup Box -->
                <div v-if="isOpenRules" id="rules-box" class="rules-box">
                    <Rules/>
                </div>
            </div>
            <!--<router-link
                v-if="$route.path === '/'"
                to="/rules"
                class="footer-link nav-item"
            >
                Rules
            </router-link>

            <router-link
                v-if="$route.path === '/rules'"
                to="/"
                class="footer-link nav-item"
            >
                Leaderboard
            </router-link>-->
        </div>

        <!-- Center: Prime Sub Message -->
        <div class="footer-center">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAACXBIWXMAAAsTAAALEwEAmpwYAAABZElEQVR4nO2Wv0rEQBDGR7BRrhDfQWsrWy0sFNHSP42l9lroGxzCvYbe7CAIPoAHdj7C4YG4MylSiO0diDmScHFDdmM8boNgBqbZnXy/fLOb7AI0USWIdwFFAIWhyztQW6AwKInSZF0fWMkgA6O81Acm2QfkrzRlq07w4Xer5aCezdKL5kFx31jjfjI2lT7+YrMgnxlu0yQ+LX9GHPq5CRk4BR6CRVASFMDxGOmFSptRmeDY/gSOMgSUNlDYKggQX1mgE8HLYn3YSrRQhhmU9LbtzXo5F8gnEEVzydz96xKgvDvBKB9Aetno4h4gvxk1j86OAPKtRfAZSK+D4mu326y2DSRroPjJMnfjBivu2AX5E1BGFcCjpNa+FJ0Sx3Lxo/i0SXJe4jg49gZGOXKDu7zpz7HeKAHLqjfwHa+4wfF3581xWPwv/PNQnlr9d8GYO6lmlFzhXmaeVLOCku1EaqIJ8BNj7Qdw+0WrSfQAAAAASUVORK5CYII=" alt="crown">
            <p>Prime Sub to
                <a href="https://www.twitch.tv/SmugDragonER" class="footer-smugdragon" target="_blank" rel="noopener noreferrer">
                    <span class="footer-smugdragon">SmugDragon</span></a>
                    for more Events!
            </p>
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAACXBIWXMAAAsTAAALEwEAmpwYAAABZElEQVR4nO2Wv0rEQBDGR7BRrhDfQWsrWy0sFNHSP42l9lroGxzCvYbe7CAIPoAHdj7C4YG4MylSiO0diDmScHFDdmM8boNgBqbZnXy/fLOb7AI0USWIdwFFAIWhyztQW6AwKInSZF0fWMkgA6O81Acm2QfkrzRlq07w4Xer5aCezdKL5kFx31jjfjI2lT7+YrMgnxlu0yQ+LX9GHPq5CRk4BR6CRVASFMDxGOmFSptRmeDY/gSOMgSUNlDYKggQX1mgE8HLYn3YSrRQhhmU9LbtzXo5F8gnEEVzydz96xKgvDvBKB9Aetno4h4gvxk1j86OAPKtRfAZSK+D4mu326y2DSRroPjJMnfjBivu2AX5E1BGFcCjpNa+FJ0Sx3Lxo/i0SXJe4jg49gZGOXKDu7zpz7HeKAHLqjfwHa+4wfF3581xWPwv/PNQnlr9d8GYO6lmlFzhXmaeVLOCku1EaqIJ8BNj7Qdw+0WrSfQAAAAASUVORK5CYII=" alt="crown">
        </div>

        <!-- Right: Contact Button -->
        <div class="footer-right">
            <div class="contact-container">
                <span @click.stop="toggleBox('Contact')" id="contact-button" class="footer-link">
                    Contact
                </span>

                <!-- Popup Box -->
                <div v-if="isOpenContact" id="contact-box" class="contact-box">
                    <p class="contact-title">In case of Issues or if you want to help:</p>
                    <p class="contact-info">Discord: <strong>SmugDragonER</strong></p>
                </div>
            </div>
        </div>
    </footer>
</template>

<style scoped>
    footer {
        font-family: Arial, Helvetica, sans-serif;
        font-size: var(--font-size-small);
        color: var(--primary-color);
        background-color: var(--background-dark-grey);

        /* Grid Layout */
        display: grid;
        grid-template-columns: 1fr auto 1fr;
        align-items: center;

        padding: 10px 20px; /* Horizontal padding for the side links */
        flex: 0 0 auto;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* SECTION ALIGNMENT */
    .footer-left {
        justify-self: start; /* Push to far left */
    }

    .footer-center {
        justify-self: center; /* Push to absolute center */
        display: flex;
        align-items: center;
        gap: var(--spacing-small);
    }

    .footer-right {
        justify-self: end; /* Push to far right */
    }

    /* LINK STYLES */
    .footer-smugdragon{
        color: var(--white-color);
        font-size: var(--font-size-medium);
        font-weight: bold;
        text-decoration: none;
    }
    .footer-smugdragon:hover {
        text-decoration: underline;
        color: var(--font-light-color)
    }

    .footer-link {
        color: var(--primary-color);
        text-decoration: none;
        cursor: pointer;
        transition: color 0.2s;
        font-weight: bold;
    }
    .footer-link:hover {
        color: #ad936e;
    }

    /* CONTACT POPUP LOGIC */
    .contact-container {
        position: relative;
    }

    .rules-box,
    .contact-box {
        position: absolute;
        bottom: 140%; /* Opens UPWARDS */
        right: 0;     /* Aligned to the right edge */

        color: var(--white-color);
        background: #2a2a2a;
        padding: 15px;
        border-radius: var(--border-radius-medium);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
        border: 1px solid #444;
        width: 220px;
        z-index: 1000;
        text-align: center;
        cursor: default;
    }

    /* Changes some properties */
    .rules-box {
        left: 0;
        width: 400px !important;
    }

    /* Arrow pointing down */
    .rules-box::after,
    .contact-box::after {
        content: "";
        position: absolute;
        top: 100%;
        border-width: 5px;
        border-style: solid;
        border-color: #2a2a2a transparent transparent transparent;
    }

    /* Manage both alignment differently */
    .contact-box::after {
        right: 15px; /* Aligns arrow with the button kinda */
    }

    .rules-box::after {
        left: 15px; /* Aligns arrow with the button kinda */
    }

    .contact-title {
        font-size: 12px;
        margin-bottom: 5px;
        opacity: 0.8;
    }

    .contact-info {
        font-size: 14px;
        color: #ad936e;
    }
</style>
