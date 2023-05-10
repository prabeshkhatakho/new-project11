import os
from pathlib import Path
import json
import pprint
import openai

file = open("my-app/src/components/data.json", "r")
config = json.load(file)
title = config[1]['title']
questions = config[1]['question']
name = config[1]['name']


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

body = ""

for question, answer  in zip(questions, answers):
  body = body + "\n<h1>{}</h1>\n<p>{}</p>".format(question, answer)



file_path = "newfile.js"


if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file_path}' already exists and has been deleted.")
js_code = """import React from 'react'

function {1}() {{
  return (
    <div>
      {0}
      {1}
    </div>
  )
}}

export default {1};

""".format(body,name)

file = Path(file_path)
file.write_text(js_code)

print(f"File '{file_path}' has been created with the JavaScript code.")
