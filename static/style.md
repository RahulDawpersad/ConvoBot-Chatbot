/* Theme variables */
:root {
    --background-color: #f7f9fc;
    --container-bg: #ffffff;
    --user-msg-bg: #dcf8c6;
    --bot-msg-bg: #f1f0f0;
    --button-bg: #007bff;
    --button-hover-bg: #0056b3;
    --text-color: #333;
}

body {
    font-family: Arial, sans-serif;
    margin: 0;
    height: 100vh;
    background-color: var(--background-color);
    color: var(--text-color);
    display: flex;
    justify-content: center;
    align-items: center;
}

.main-container {
    width: 100%;
    height: 100%;
    display: flex;
    background-color: var(--background-color);
}

.sidebar {
    width: 250px; /* Adjust the width as needed */
    /* background-color: var(--container-bg); */
    background: #171717;
    padding: 20px;
    box-sizing: border-box;
}


.sidebar .sidebar-content{
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 2em 0;
}

.sidebar .sidebar-content .img-fluid{
    width: 60px;
    height: 60px;
}

.sidebar .sidebar-content h1 {
    color: #f1f0f0;
    font-size: 1.5em;
    margin-bottom: 10px;
}

.sidebar p {
    color: #dcf8c6;
    font-size: 1em;
    line-height: 1.4;
    margin: 2em 0;
}

.chat-container {
    flex: 1;
    display: flex;
    flex-direction: column;
    height: 100%;
    background-color: var(--container-bg);
}

.chat-box {
    background: #212121;
    flex: 1;
    padding: 30px;
    overflow-y: auto;
}


.chat-box .logo-container{
    text-align: center;
}

.chat-box .logo-container .heading{
    font-size: 2em;
}


.chat-box .logo-container p{
    font-size: 0.9em;
    text-align: center;
}

.chat-box p {
    margin: 10px 0;
    padding: 10px;
    border-radius: 10px;
    max-width: 90%;
    word-wrap: break-word;
}

.user-message {
    background-color: var(--user-msg-bg);
    align-self: flex-end;
    text-align: left;
    width: 230px;
}

.bot-response {
    background-color: var(--bot-msg-bg);
}

.input-form {
    position: fixed;
    bottom: 0;
    width: 80%;
    max-width: 1200px;
    /* background-color: var(--container-bg); */
    background: #212121;
    /* border-top: 1px solid #ddd; */
    padding: 10px;
    box-sizing: border-box;
    display: flex;
    justify-content: center;
    align-items: center;
}

.input-container {
    display: flex;
    width: 80%;
    padding: 10px;
    box-sizing: border-box;
}

input[type="text"] {
    color: #dcf8c6;
    flex: 1;
    padding: 15px;
    /* border: 1px solid #ddd; */
    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
    font-size: 1em;
    border: 0;
    background: #2F2F2F;
    border-radius: 20px;
    margin-right: 10px;
    outline: none;
}

button {
    padding: 10px 20px;
    border: none;
    background-color: var(--button-bg);
    color: white;
    cursor: pointer;
    border-radius: 20px;
    display: flex;
    align-items: center;
}

/* button:hover {
    background-color: var(--button-hover-bg);
} */

button i {
    margin-left: 5px;
}

.delete-button{
    background: none;
}

.error-message {
    color: red;
    text-align: center;
}

.menu-button {
    display: none; /* Hide the menu button by default */
    position: fixed;
    font-size: 1.4em;
    top: 10px;
    left: 10px;
    padding: 10px 20px;
    /* background-color: var(--button-bg); */
    background: transparent;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    z-index: 1000;
}

@media only screen and (max-width: 767px) {
    .sidebar {
        display: none; /* Hide the sidebar by default on mobile devices */
        position: fixed;
        top: 0;
        left: 0;
        height: 100%;
        width: 250px;
        background: #171717;
        padding: 48px;
        box-sizing: border-box;
        z-index: 999;
        transform: translateX(-100%);
        transition: transform 0.3s ease;
    }

    .sidebar.active {
        display: block;
        transform: translateX(0);
    }

    .menu-button {
        display: block; /* Show the menu button on smaller screens */
    }

    /* .input-form {
        width: 100%;
    } */
    /* .input-form {
        position: fixed;
        bottom: 0;
        width: calc(100% - 250px);
        max-width: 100%;
        background-color: var(--container-bg);
        border-top: 1px solid #ddd;
        padding: 10px;
        box-sizing: border-box;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1;
    }

    .input-container {
        padding: 10px;
    }
    .chat-box {
        max-height: calc(100vh - 160px);
    } */
    .input-container {
        display: flex;
        width: 100%;
        padding: 10px;
        box-sizing: border-box;
        max-width: calc(100% - 120px); /* Adjust as needed */
    }

    input[type="text"] {
        flex: 1;
        padding: 10px;
        /* border: 1px solid #ddd; */
        border: none;
        border-radius: 20px;
        margin-right: 10px;
        outline: none;
        width: 80%; /* Adjust the width as needed */
    }

    .chat-box {
        flex: 1;
        padding: 20px;
        overflow-y: auto; /* Enable vertical scrolling */
        max-height: calc(100vh - 100px); /* Adjust as needed */
    }
    
    .input-form {
        position: fixed;
        bottom: 0;
        width: 100%;
        max-width: 1200px; /* Adjust as needed */
        background: #212121;
        padding: 10px;
        box-sizing: border-box;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .sidebar .sidebar-content{
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 1em 0;
    }

    .sidebar p {
        font-size: 0.9em;
        margin: 1em -1em;
        width: 200px;
    }
}

@media (min-width: 768px) and (max-width: 1344px) {
    .sidebar {
        width: 200px; /* Adjust the width for tablet view if needed */
    }
    .input-container {
        display: flex;
        width: 70%;
        margin-left: -10em;
        padding: 10px;
        box-sizing: border-box;
        max-width: calc(100% - 120px); /* Adjust as needed */
    }
    
    .chat-box {
        flex: 1;
        padding: 20px;
        overflow-y: auto; /* Enable vertical scrolling */
        max-height: calc(100vh - 100px); /* Adjust as needed */
    }
    
    .input-form {
        position: fixed;
        bottom: 0;
        width: 100%;
        max-width: 1200px; /* Adjust as needed */
        background: #212121;
        border: none;
        padding: 10px;
        box-sizing: border-box;
        display: flex;
        justify-content: center;
        align-items: center;
    }
}
