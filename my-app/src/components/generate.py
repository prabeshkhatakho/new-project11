import json
import pprint
import openai






file = open("my-app/src/components/data.json", "r")
data = json.load(file)
title = data[0]['title']
question = data[0]['question']
name = data[0]['name']

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

print(message + "hello")


pprint.pprint(data)

js_code = '''
import React from 'react'

function washingmachine() {{
  return (
    <div>
      <h1>{0}</h1>
      <h1>{1}</h1>
      <h1>{2}</h1>
      <p>{3}</p>
    </div>
  )
}}

export default washingmachine;

'''.format(name,title,question,message)

with open('newfile.js', 'w') as file:
    file.write(js_code)
    file.close()
