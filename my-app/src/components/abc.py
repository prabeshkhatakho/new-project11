import json
import pprint
import openai

file = open("my-app/src/components/data.json", "r")
data = json.load(file)
title = data[0]['title']
questions = data[0]['question']
name = data[0]['name']




questions = []
answers = []


for question in questions:

  openai.api_key = "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"

  prompt = f"{question}"
  response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
  max_tokens=50,
  n=1,
  stop=None,
  temperature=0.5,
  )


  message = response.choices[0].text.strip()
  answers.append(message)
  
print(answers)

questions.append(question)
print(questions)

body = ""

for question, answer  in zip(questions, answers):
  body = body + "\n<h1>{}</h1>\n<p>{}</p>".format(question, answer)




js_code = '''
import React from 'react'

function washingmachine() {{
  return (
    <div>
      
      {0}
    </div>
  )
}}



'''.format(body)

with open('newfile.js', 'w') as file:
    file.write(js_code)
    file.close()