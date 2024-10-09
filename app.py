import os
from dotenv import load_dotenv
import openai
from flask import Flask, request, jsonify

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

def evaluate_code(code): 
    prompt = f"""evaluate the code:
    {code} 
    with Correctness,efficiency,Code Quality,time complexity,Problem-Solving Approach, don't display the output"""
    response = openai.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",  # Use a chat model like gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "you are a coding assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=4000,  # Adjust max_tokens based on desired response length
        temperature=0.5  # Adjust temperature as needed
    )
    feedback = response.choices[0].message.content.strip()
    return feedback

app = Flask(__name__)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    if not request.json or 'code' not in request.json:
        return jsonify({'error': 'No code provided'}), 400
    
    user_solution = request.json['code']
    feedback = evaluate_code(user_solution)
    return jsonify({'feedback': feedback})

if __name__ == "__main__":
    app.run(debug=True)
