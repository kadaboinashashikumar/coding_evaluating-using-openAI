# @title install openAI
#!pip install openai


#@title openai_key and Import

import openai

api_key = 'ysdfksk;ljdf' #enter your api key
openai.api_key = api_key





#@title evaluating code
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
        max_tokens=4000,# Adjust max_tokens based on desired response length
        temperature=0.5# Convert the dictionary values to a list of lists

    )

  feedback = response.choices[0].message.content.strip()
  return feedback







#@title Flask app
from markupsafe import escape

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='/content/drive/MyDrive/templates')

@app.route('/')
def index():
     
    c="This a coding test, Enter the solution below"
    return render_template('index.html', question=c)

@app.route('/submit', methods=['POST'])
def submit():
    user_solution = request.form['solution']
    feedback = evaluate_code(user_solution)
    f=escape(feedback)

    return render_template('feedback.html', feedback=f)

if __name__ == "__main__":
    app.run()
