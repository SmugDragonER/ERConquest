<script>
export default {
    name: "Header",
    components: {
    },
    data() {
        return {
        };
    },
    watch: {
    },
    computed: {
    },
    methods: {
    },
}
</script>

<template>
    <header>
        <div class="left-header">
        </div>

        <div>
            <p id="last-updated">Loading last updated time...</p>
        </div>

        <div class="right-header">
        </div>
    </header>
</template>

<style>
    /* Header Styles */
    header {
        position: sticky; /* Makes the header sticking the position even after scrolling */
        top: 0;
        font-family: Arial, Helvetica, sans-serif;
        font-size: var(--font-size-small);
        color: var(--primary-color);
        display: flex;
        justify-content: space-between;
        padding-left: var(--spacing-medium);
        padding-right: var(--spacing-medium);
        align-items: center;
        background-color: var(--background-dark-grey);
        flex: 0, 0, auto;
        z-index: 99;
    }
    header div {
        width: 33%;
    }

    .left-header {
        text-align: left;
    }

    .right-header {
        text-align: right;
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
</style>
