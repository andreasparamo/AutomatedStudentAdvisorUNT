from flask import Flask, request, jsonify, render_template


import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("GENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set GENAI_API_KEY in the .env file.")

# Configure the generative AI library
genai.configure(api_key=api_key)

# Use the model
model = genai.GenerativeModel("gemini-1.5-flash")



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bot.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    # Here you can implement your logic to generate a response based on the user_message
    response = model.generate_content(user_message)
    bot_response = response.text
    return jsonify(response=bot_response)

if __name__ == '__main__':
    app.run(debug=True)