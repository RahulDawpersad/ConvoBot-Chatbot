from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_cors import CORS
import os
import cohere
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS

# Secure secret key (ensure this is set correctly in a production environment)
app.secret_key = os.urandom(24)

# Set your Cohere API key from environment variable or default (make sure to set this on Vercel)
API_KEY = os.getenv('COHERE_API_KEY', 'ABFUK8eB4APHixJyTeox5YbgBYAaEN9K44CN3iLm')

# Initialize the Cohere client
co = cohere.Client(API_KEY)

# Define approximate response time (in seconds)
APPROX_RESPONSE_TIME = 9

def ask_question(question):
    try:
        # Use the Cohere API to generate a response
        response = co.generate(
            model='command',
            prompt=f"{question}\n",
            max_tokens=500,  # Increase tokens to allow detailed response
            temperature=0.9,  # Controls randomness; lower value makes responses more deterministic
            stop_sequences=["\n"]  # Ensure the response stops at a sensible point
        )

        # Extract and return the response
        generated_text = response.generations[0].text.strip()
        return generated_text

    except Exception as e:
        app.logger.error(f"Error in ask_question: {e}")
        return f"An error occurred: {e}"

@app.route("/", methods=["GET", "POST"])
def chat():
    if 'chat_history' not in session:
        session['chat_history'] = []

    if request.method == "POST":
        user_input = request.form["user_input"]
        
        # Display approximate response time to the user
        response_message = f"Your question is being processed. Approximate response time: {APPROX_RESPONSE_TIME} seconds."
        session['chat_history'].append({"user": user_input, "bot": response_message})
        
        # Generate response asynchronously
        response = ask_question(user_input)
        
        # Update chat history with actual response
        session['chat_history'][-1]["bot"] = response
        
        session.modified = True
        return redirect(url_for('chat'))

    return render_template("index.html", chat_history=session['chat_history'])

@app.route("/delete_message", methods=["POST"])
def delete_message():
    try:
        data = request.json
        index = int(data.get('index', -1))  # Use default value -1 if index is not found
        if 'chat_history' in session and 0 <= index < len(session['chat_history']):
            del session['chat_history'][index]
            session.modified = True
            return jsonify({'success': True}), 200
        else:
            return jsonify({'success': False, 'error': 'Invalid index'}), 400
    except Exception as e:
        app.logger.error(f"Error in delete_message: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True)
