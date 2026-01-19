<script>
import Rules from '../views/Rules.vue';

export default {
    name: "Header",
    components: { Rules },
    data() {
        return {
            isOpenContact: false,
            isOpenRules: false
        };
    },
    watch: {
        isOpenContact(val) { this.handleListener(val); },
        isOpenRules(val) { this.handleListener(val); }
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

            if (contactBox && !contactBox.contains(event.target) && event.target !== contactBtn) {
                this.closeBox("Contact");
            }
            if (rulesBox && !rulesBox.contains(event.target) && event.target !== rulesBtn) {
                this.closeBox("Rules");
            }
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
            <div class="popup-wrapper">
                <span @click.stop="toggleBox('Rules')" id="rules-button" class="nav-link">Rules</span>
                <div v-if="isOpenRules" id="rules-box" class="dropdown-box rules-wide">
                    <Rules/>
                </div>
            </div>

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
        gap: 20px;
        justify-content: space-between;
        width: 100%;
    }

    .nav-link {
        color: var(--primary-color);
        font-weight: bold;
        cursor: pointer;
        transition: color 0.2s;
        justify-content: space-between;
        width: auto;
    }

    .nav-link:hover { color: #ad936e; }

    .popup-wrapper { position: relative; }

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
