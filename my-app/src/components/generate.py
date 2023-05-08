import json
import pprint


def generate_js_file(config):
  title = config['title']
  questions = config['question']
  name = config['name']
  filename = config['name'] + ".js"

  pprint.pprint(config)

  #questions = ["question1", "question2", "question3"]
  answers = []

  # get answers for all questions and store that in answers
  for question in questions:
    chatgpt_resonse = "response"
    answers.append(chatgpt_resonse)

  #create string html for questions and answers

  body = ""

  for question, answer  in zip(questions, answers):
    body = body + "\n<h1>{}</h1>\n<p>{}</p>".format(question, answer)


  js_code = '''
  import React from "react"

  function washingmachine() {{
    return (
      <div>
        {1}
      </div>
    )
  }}

  export default {2};

  '''.format(title,body , name)

  with open(filename, 'w') as file:
      file.write(js_code)
      file.close()



def process_configs():
  file = open("my-app/src/config/pages-config.json", "r")
  configs = json.load(file)

  for config in configs:
    (generate_js_file(config))

process_configs()


