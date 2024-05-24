from flask import Flask, request, jsonify
from g4f.client import Client
from g4f.Provider import DuckDuckGo

app = Flask(__name__)

# Initialize OpenAI Client
client = Client()

@app.route('/')
def home():
    return "Welcome to the DuckDuckGo Chat API!"

@app.route('/chat', methods=['GET'])
def chat():
    question = request.args.get('question')

    if not question:
        return jsonify({"error": "Please provide a question parameter in the URL."})

    # Call GPT-3 to generate a response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
    )

    return jsonify({"response": response.choices[0].message.content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
