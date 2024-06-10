import cohere
 
 # Set your Cohere API key
API_KEY = 'ABFUK8eB4APHixJyTeox5YbgBYAaEN9K44CN3iLm'

# Initialize the Cohere client
co = cohere.Client(API_KEY)

def ask_question(question):
    try:
        # Use the Cohere API to generate a response
        response = co.generate(
            model='c4ai-aya-23',
            #  model='command',
            prompt=question,
            max_tokens=250,
            temperature=1,  # Controls randomness; lower value makes responses more deterministic
            stop_sequences=["\n"]  # Ensure the response stops at a sensible point
        )

        # Extract and print the response
        generated_text = response.generations[0].text.strip()
        return generated_text

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    while True:
        question = input("Ask Cohere a question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        response = ask_question(question)
        print(f"Cohere AI: {response}\n")