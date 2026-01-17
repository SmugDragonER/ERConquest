<template>
    <!-- Empty template to remove the header bar completely, commented the old Header for now -->
    <header style="display: none;"></header>
</template>

<!--
<script>
export default {
    name: "Header",
    components: {
    },
    data() {
        return {
            isOpen: false //shows "Contact"- Box
        };
    },
    watch: {
        isOpen (val) {
            if (val) {
                document.addEventListener("click", this.handleClickOutside);
            } else {
                document.removeEventListener("click", this.handleClickOutside);
            }
        }
    },
    computed: {
    },
    methods: {
        toggleBox() {
            this.isOpen = !this.isOpen;
        },
        closeBox() {
            this.isOpen = false;
        },
        handleClickOutside(event) {
            if (event?.target?.id != "contact-box") {
                this.closeBox();
            }
        }
    },
}
</script>

<template>
    <header>


    <nav class="header-nav">
        <!-- Show RULES link only on the leaderboard page -->
         <!--
        <router-link
            v-if="$route.path === '/'"
            to="/rules"
            class="nav-item"
        >
            Rules
        </router-link>

        <!-- Show LEADERBOARD link only on the rules page -->
         <!--
        <router-link
            v-if="$route.path === '/rules'"
            to="/"
            class="nav-item"
        >
            Leaderboard
        </router-link>
    </nav>


        <div class="contact-container">
            <p
                @click.stop="toggleBox"
                id="contact-button"
                class="contact-text"
            >
                Contact
            </p>

            <div
                v-if="isOpen"
                id="contact-box"
                class="contact-box"
            >
                <p>In case of Issues or if you want to help:</p>
                <p>Discord: SmugDragonER</p>
            </div>
        </div>
    </header>
</template>

<style>
    /* Header Styles */
header {
    font-family: Arial, Helvetica, sans-serif;
    font-size: var(--font-size-small);
    color: var(--primary-color);
    padding-left: var(--spacing-medium);
    padding-right: var(--spacing-medium);
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: var(--background-dark-grey);
    flex: 0, 0, auto;
}

    .header-nav {
    display: flex;
    gap: 1.5rem;
    }

    .nav-item {
    color: var(--primary-color);
    font-family: Arial, Helvetica, sans-serif;
    font-size: var(--font-size-small);
    cursor: pointer;
    text-decoration: none;
    }

    .nav-item:hover {
        color: #ad936e; /* same hover as your contact text */
    }

    .contact-container {
        position: relative;
        display: inline-block;
    }

    .contact-text {
        cursor: pointer;
        display: inline-block;
        text-decoration: none;
        transition: color 0.3s ease;
    }

    .contact-text:hover {
        color: #ad936e;
    }
    /*not working atm*/
    .contact-box {
        position: absolute;
        top: 100%;  /* Position dropdown right below the button */
        right: 0;
        color: var(--white-color);
        background: var(--background-dark-grey);
        padding: var(--spacing-small);
        border-radius: var(--border-radius-medium);
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        width: 220px;
        z-index: 1000;
    }
    .box { padding: 20px; background: #eee; border: 1px solid #aaa; margin-top: 10px; }
</style>
-->
