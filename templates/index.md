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
    function validateForm() {
      var userInput = document.getElementById("user_input").value;
      if (userInput.trim() === "") {
        document.getElementById("error_message").innerText = "Please enter text.";
        return false;
      }
      return true;
    }

    function toggleSidebar() {
      var sidebar = document.querySelector(".sidebar");
      sidebar.classList.toggle("active");
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
          if (response.ok) {
            location.reload(); // For example, reload the page
          } else {
            console.error('Error deleting message');
          }
        })
        .catch(error => {
          console.error('Error:', error);
        });
    }

    function copyToClipboard(text) {
      // Create a temporary textarea element
      const tempTextArea = document.createElement('textarea');
      tempTextArea.value = text;
      document.body.appendChild(tempTextArea);

      // Select the text and copy it
      tempTextArea.select();
      document.execCommand('copy');

      // Remove the temporary textarea element
      document.body.removeChild(tempTextArea);

      alert("Text copied to clipboard");
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
    </div>
    <div class="chat-container">
      <div class="chat-box" id="chat-box">
        <div class="logo-container">
          <p class="heading">DESIGNX</p>
          <p>Developed By Rahul Dawpersad</p>
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
            <button class="copy-button" title="Copy Text" onclick="copyToClipboard('{{ message.bot | e | replace(" \'", "\\\'" ) |
              replace("\"", "\\\"") }}')">
              <i class="fa-solid fa-copy"></i>
            </button>
            <button class="share-button"
            title="Share" onclick="shareResponse('{{ message.user }}', '{{ message.bot }}')"><i class="fa-solid fa-share"></i></button>
          </div>
          {% endif %}
        </div>
        {% endfor %}
      </div>
      <form method="post" onsubmit="return validateForm()" class="input-form">
        <div class="input-container">
          <input type="text" id="user_input" name="user_input" placeholder="Message ConvoBot" autocomplete="off"
            oninput="adjustWidth()" class="dynamic-input" />
          <button type="submit">
            Send <i class="fa-solid fa-paper-plane"></i>
          </button>
        </div>
        <p id="error_message" class="error-message"></p>
      </form>
    </div>
  </div>
  <button class="menu-button" onclick="toggleSidebar()"><i class="fa-solid fa-bars"></i></button>

  
</body>

</html>