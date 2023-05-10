import os
from pathlib import Path
import json
import pprint
import openai

file = open("my-app/src/components/data.json", "r")
configs = json.load(file)
body = ""
links = []

for config in configs:
  print(f'config {config}')
  questions = config['questions']
  answers = []
  name = config['name']
  title = config['title']
  links.append(f'<Link to=\'{name}\'>{name}</Link>')
  for question in questions:
    openai.api_key = "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"
    prompt = f"{question}"
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5)
    message = response.choices[0].text.strip()
    answers.append(message)
  
  for question, answer in zip(questions, answers):
    body = body + "\n<h1>{}</h1>\n<p>{}</p>".format(question, answer)


  file_path = f"{name}.js"


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



print(links)
##generate home.js




# answers = []

# for question in questions:
#   openai.api_key = "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"

#   prompt = f"{question}"
#   response = openai.Completion.create(
#   engine="text-davinci-002",
#   prompt=prompt,
#   max_tokens=50,
#   n=1,
#   stop=None,
#   temperature=0.5,
#   )

#   message = response.choices[0].text.strip()

#   answers.append(message)
# print(answers)

# body = ""

# for question, answer  in zip(questions, answers):
#   body = body + "\n<h1>{}</h1>\n<p>{}</p>".format(question, answer)



# file_path = "newfile.js"


# if os.path.exists(file_path):
#     os.remove(file_path)
#     print(f"File '{file_path}' already exists and has been deleted.")
# js_code = """import React from 'react'

# function {1}() {{
#   return (
#     <div>
#       {0}
#       {1}
#     </div>
#   )
# }}

# export default {1};

# """.format(body,name)

# file = Path(file_path)
# file.write_text(js_code)

# print(f"File '{file_path}' has been created with the JavaScript code.")
