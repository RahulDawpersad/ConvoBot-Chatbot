@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

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
  font-family: "Poppins", sans-serif;
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
  /* background-color: var(--background-color); */
}

.sidebar {
  width: 250px; /* Adjust the width as needed */
  /* background-color: var(--container-bg); */
  background: #AF0404;
  /* background: #205295; */
  padding: 20px;
  box-sizing: border-box;
}

.sidebar .sidebar-content {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 2em 0;
}

.sidebar .sidebar-content .img-fluid {
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
  font-size: 0.9em;
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
  /* background: #212121;
    flex: 1;
    padding: 30px;
    overflow-y: auto; */
  background: #212121;
  /* background: linear-gradient(90deg, #141e30, #243b55); */
  flex: 1;
  padding: 20px;
  overflow-y: auto; /* Enable vertical scrolling */
  max-height: calc(100vh - 120px); /* Adjust as needed */
}

.chat-box .logo-container {
  text-align: center;
}

.chat-box .logo-container .heading {
  font-size: 2em;
}

.chat-box .logo-container p {
    color: #535353;
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
  /* background-color: var(--user-msg-bg); */
  color: #f1f0f0;
  background: #AF0404;
  align-self: flex-end;
  text-align: left;
  width: 300px;
}

.bot-response {
  background-color: var(--bot-msg-bg);
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
  /* position: fixed;
    bottom: 0;
    width: 80%;
    max-width: 1200px; */
  /* background-color: var(--container-bg); */
  /* background: #212121; */
  /* border-top: 1px solid #ddd; */
  /* padding: 10px;
    box-sizing: border-box;
    display: flex;
    justify-content: center;
    align-items: center; */
}

.input-container {
  /* display: flex;
    width: 80%;
    padding: 10px;
    box-sizing: border-box; */
  display: flex;
  width: 80%;
  margin-left: -5em;
  padding: 10px;
  box-sizing: border-box;
  max-width: calc(100% - 120px); /* Adjust as needed */
}

input[type="text"] {
  display: flex;
  align-items: center;
  color: #dcf8c6;
  flex: 1;
  padding: 15px;
  /* border: 1px solid #ddd; */
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
  font-size: 1em;
  border: 0;
  background: #2f2f2f;
  border-radius: 20px;
  margin-right: 10px;
  outline: none;
}

button {
  padding: 10px 20px;
  border: none;
  background: #AF0404;
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

.logo-container .link{
    color: #AF0404;
    text-decoration: none;
    transition: .1s ease-in;
}

.logo-container .link:hover{
    color: #AF0404;
    text-decoration: underline;
}


.copy-button, .delete-button, .share-button {
    margin-left: 5px;
    padding: 5px 10px;
    background-color: #212121;
    color: #FF0000;
    border: none;
    cursor: pointer;
  }

.message-buttons {
    display: inline-flex;
    align-items: center;
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
    /* background: #171717; */
    background: #AF0404;
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
    margin-left: 1em;
    width: 100%;
    padding: 10px;
    box-sizing: border-box;
    max-width: calc(100% - 60px);
  }

  input[type="text"] {
    flex: 1;
    padding: 10px;
    /* border: 1px solid #ddd; */
    border: none;
    border-radius: 20px;
    margin-right: 10px;
    outline: none;
    width: 90%; /* Adjust the width as needed */
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
  .sidebar .sidebar-content {
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
    max-height: calc(100vh - 120px); /* Adjust as needed */
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


/* How to change the  color of the scrollbar */

::-webkit-scrollbar{
    width: 10px;
}

::-webkit-scrollbar-thumb{
    background: #AF0404;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover{
    background: #AF0404;
}


.notification {
  visibility: hidden;
  min-width: 250px;
  background-color: #333;
  color: #fff;
  text-align: center;
  border-radius: 2px;
  padding: 8px;
  position: absolute;
  z-index: 1;
  font-size: 14px;
}

.notification.show {
  visibility: visible;
  animation: fadein 0.5s, fadeout 0.5s 2.5s;
}

@keyframes fadein {
  from {opacity: 0;}
  to {opacity: 1;}
}

@keyframes fadeout {
  from {opacity: 1;}
  to {opacity: 0;}
}