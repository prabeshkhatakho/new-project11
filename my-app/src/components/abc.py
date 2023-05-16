import json
import pprint
import openai
import os
from pathlib import Path


file = open("my-app/src/components/data.json", "r")
datas = json.load(file)
links = []





for data in datas:
  
  title = data['title']
  questions = data['questions']
  answers = []
  
  body = ""
  name = data['name']
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
    temperature=0.5,
    )

    message = response.choices[0].text.strip()
    answers.append(message)

  for question, answer  in zip(questions, answers):
    
    body = body + "\n<h1>{}</h1>\n<p>{}</p>".format(question, answer)

  file_path = f"{name}.js"
  
  if os.path.exists(file_path):
      os.remove(file_path)
      print(f"File '{file_path}' already exists and has been deleted.")

  js_code = '''
  import React from 'react'

  function {1}() {{
    return (
      <div>
        
        {0}
      </div>
    )
  }}

  export default {1};

  '''.format(body,name)

  file = Path(file_path)
  file.write_text(js_code, encoding='utf-8')
  print(f"File '{file_path}' has been created with the JavaScript code.")

  #this is a break line

home_path = f"home.js"

links_code = "\n".join(links)
  
  
if os.path.exists(home_path):
  os.remove(home_path)
  print(f"File '{home_path}' already exists and has been deleted.")

home_js_code = '''
  import React from 'react'
  import {{Link}} from 'react-router-dom'

  function Home() {{
    return (
      <div>
        
        {0}
      </div>
    )
  }}
  export default Home;
  '''.format(links_code)

file = Path(home_path)
file.write_text(home_js_code, encoding='utf-8')
print(f"File '{home_path}' has been created with the JavaScript code.")

  
print(links)
  
  
 

  

  
 

   