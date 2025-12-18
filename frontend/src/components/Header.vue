<script></script>


<template>
    <header>
        <p id="last-updated">Loading last updated time...</p>
        <div class="contact-container">
            <p id="contact-button" class="contact-text">Contact</p>
            <div id="contact-box" class="contact-box">
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
    font-size: smaller;
    color: var(--primary-color);
    padding-left: var(--spacing-medium);
    padding-right: var(--spacing-medium);
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: var(--background-dark-grey);
    flex:1;
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

    .contact-box {
        display: none;
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

    .lurkLogo {
        width: 100px;
        height: 100px;
    }
</style>