import os
from pathlib import Path
import json
import pprint

file = open("my-app/src/components/data.json", "r")
config = json.load(file)
title = config[1]['title']
question = config[1]['question']
name = config[1]['name']



pprint.pprint(config)


file_path = "newfile.js"


if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file_path}' already exists and has been deleted.")
js_code = """import React from 'react'

function language() {{
  return (
    <div>
      <h1>{0}</h1>
      <p>{1[0]}</p>
        <br></br>
        <h1>{1[1]}</h1>
        <p></p>
        <br></br>
        <h1>{1[2]}</h1>
        <p></p>
    </div>
  )
}}

export default language

""".format(name,question)

file = Path(file_path)
file.write_text(js_code)

print(f"File '{file_path}' has been created with the JavaScript code.")
