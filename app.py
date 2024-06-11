from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import os
import cohere

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a secure secret key

# Set your Cohere API key
API_KEY = 'ABFUK8eB4APHixJyTeox5YbgBYAaEN9K44CN3iLm'

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
        index = int(request.json['index'])
        print('Deleting message at index:', index)
        if 'chat_history' in session and 0 <= index < len(session['chat_history']):
            del session['chat_history'][index]
            session.modified = True
            return jsonify({'success': True}), 200
        else:
            return jsonify({'success': False, 'error': 'Invalid index'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
