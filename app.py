# @title install openAI
#!pip install openai


#@title openai_key and Import

import openai

api_key = 'ysdfksk;ljdf' #enter your api key
openai.api_key = api_key





#@title generating question
def generate_problem_statement(input_text):
    # Prompt for GPT-3
  prompt = input_text

    # Parameters for GPT-3 completion
  response = openai.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",  # Use a chat model like gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=4000,
        temperature=0.5# Adjust max_tokens based on desired response length
    )

    # Extract and return feedback from GPT-3 response
  feedback = response.choices[0].message.content.strip()
  return feedback


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






#optional_output

"""query=f"Generate a programming problem suitable for a coding test with test cases, time complexity and can be solved in any programming language "
coding_question=generate_problem_statement(query)
print(coding_question)


user_solution=input("enter the solution")

feedback = evaluate_code(user_solution) 
print(feedback)"""



#@title Flask app
from markupsafe import escape

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='/content/drive/MyDrive/templates')

@app.route('/')
def index():
    global coding_question
    query=f"Generate a programming problem suitable for a coding test with test cases, time complexity and can be solved in any programming language "
    coding_question=generate_problem_statement(query)
    c=escape(coding_question)
    return render_template('index.html', question=c)

@app.route('/submit', methods=['POST'])
def submit():
    user_solution = request.form['solution']
    #feedback = evaluate_code(coding_question,user_solution)
    feedback = evaluate_code(user_solution)
    f=escape(feedback)

    return render_template('feedback.html', feedback=f)

if __name__ == "__main__":
    app.run()