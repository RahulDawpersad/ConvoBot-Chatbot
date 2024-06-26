<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Chatbot</title>
  <link rel="shortcut icon" href="../static/img/chatbot1.png" type="image/x-icon" />
  <script src="https://kit.fontawesome.com/655b3b7e45.js" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="../static/style.css" />
  <script>
    function scrollToBottom() {
      var chatBox = document.getElementById("chat-box");
      chatBox.scrollTop = chatBox.scrollHeight;
    }

    function addMessage(user, bot) {
      var chatBox = document.getElementById("chat-box");

      var userMessage = document.createElement("div");
      userMessage.className = "user-message";
      userMessage.innerHTML = '<i class="fa-solid fa-user"></i> ' + user;
      chatBox.appendChild(userMessage);

      var botResponse = document.createElement("div");
      botResponse.className = "bot-response";
      botResponse.innerHTML = '<i class="fa-solid fa-robot"></i> ' + bot;
      chatBox.appendChild(botResponse);

      scrollToBottom();
    }

    function validateForm(event) {
      event.preventDefault();

      var userInput = document.getElementById("user_input").value;
      if (userInput.trim() === "") {
        document.getElementById("error_message").innerText = "Please enter text.";
        return false;
      }
      document.getElementById("chatForm").submit();
    }

    function toggleSidebar() {
      var sidebar = document.querySelector(".sidebar");
      var menuButton = document.querySelector(".menu-button");
      sidebar.classList.toggle("active");
      menuButton.classList.toggle("active");
    }

    function deleteMessage(index) {
      console.log('Deleting message at index:', index);
      fetch('/delete_message', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ index: index }),
      })
      .then(response => {
        console.log('Response status:', response.status);
        return response.json();
      })
      .then(data => {
        console.log('Response data:', data);
        if (data.success) {
          location.reload();
        } else {
          console.error('Error deleting message:', data.error);
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
    }

    // function copyToClipboard(text) {
    //   const tempTextArea = document.createElement('textarea');
    //   tempTextArea.value = text;
    //   document.body.appendChild(tempTextArea);

    //   tempTextArea.select();
    //   document.execCommand('copy');

    //   document.body.removeChild(tempTextArea);

    //   alert("Text copied to clipboard");
    // }
    function copyToClipboard(text, event) {
  const tempTextArea = document.createElement('textarea');
  tempTextArea.value = text;
  document.body.appendChild(tempTextArea);

  tempTextArea.select();
  document.execCommand('copy');

  document.body.removeChild(tempTextArea);

  // Create and show the notification
  const notification = document.createElement('div');
  notification.className = 'notification show';
  notification.innerText = 'Text copied to clipboard';

  // Position the notification just below the button
  const rect = event.target.getBoundingClientRect();
  notification.style.top = `${rect.bottom + window.scrollY + 10}px`;
  notification.style.left = `${rect.left + window.scrollX}px`;

  document.body.appendChild(notification);

  // Hide the notification after 3 seconds
  setTimeout(() => {
    notification.className = notification.className.replace('show', '');
    document.body.removeChild(notification);
  }, 3000);
}


    function shareResponse(userMessage, botResponse) {
      console.log("User Message:", userMessage);
      console.log("Bot Response:", botResponse);
      var message = "User Message: " + userMessage + "\n" + "Bot Response: " + botResponse;
      if (navigator.share) {
        navigator.share({
          title: "Chatbot Conversation",
          text: message,
          url: window.location.href
        }).then(() => {
          console.log("Shared successfully");
        }).catch((error) => {
          console.error("Error sharing:", error);
        });
      } else {
        alert("Web Share API is not supported in this browser or on non-HTTPS websites. Try using a different browser or test on a live server.");
      }
    }
  </script>
</head>

<body>
  <div class="main-container">
    <div class="sidebar">
      <div class="sidebar-content">
        <h1>ConvoBot</h1>
        <img src="../static/bot.gif" class="img-fluid" alt="">
      </div>
      <p>My chatbot only generates limited text upon the question asked.
        It does not generate code or massive amounts of text as it is a
        pretrained model trained on limited data.
      </p>
      <p>ConvoBot typically responds within approximately 9 seconds. 
          Please be patient while waiting for the response.</p>
    </div>
    <div class="chat-container">
      <div class="chat-box" id="chat-box">
        <div class="logo-container">
          <p class="heading">DESIGNX</p>
          <p>Developed By <a href="#" class="link">Rahul Dawpersad</a></p>
        </div>
        {% for message in chat_history %}
        <div>
          <p class="user-message">
            <i class="fa-solid fa-user"></i> {{ message.user }}
          </p>
          <p class="bot-response">
            <i class="fa-solid fa-robot"></i> {{ message.bot }}
          </p>
          {% if message.bot %}
          <div class="message-buttons">
            <button class="delete-button" title="Delete" onclick="deleteMessage({{ loop.index0 }})">
              <i class="fa-solid fa-trash"></i>
            </button>
            <!-- <button class="copy-button" title="Copy Text" onclick="copyToClipboard('{{ message.bot | e | replace(" \'", "\\\'" ) | replace("\"", "\\\"") }}')"> -->
              <button class="copy-button" title="Copy Text" onclick="copyToClipboard('{{ message.bot | e | replace(" \'", "\\\'" ) | replace("\"", "\\\"") }}', event)">
              <i class="fa-solid fa-copy"></i>
            </button>
            <button class="share-button" title="Share" onclick="shareResponse('{{ message.user }}', '{{ message.bot }}')">
              <i class="fa-solid fa-share"></i>
            </button>
          </div>
          {% endif %}
        </div>
        {% endfor %}
      </div>
      <form id="chatForm" method="post" onsubmit="return validateForm(event)" class="input-form">
        <div class="input-container">
          <input type="text" id="user_input" name="user_input" placeholder="Message ConvoBot" autocomplete="off" oninput="adjustWidth()" class="dynamic-input" />
          <button type="submit">
            Send <i class="fa-solid fa-paper-plane"></i>
          </button>
        </div>
        <p id="error_message" class="error-message"></p>
      </form>
    </div>
  </div>
  <button class="menu-button" onclick="toggleSidebar()"><i class="fa-solid fa-bars"></i></button>


  <script>
    window.onload = scrollToBottom;
  </script>
</body>

</html>
