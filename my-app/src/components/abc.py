import json

# Open the JSON file and read its contents
with open("my-app/src/components/data.json", "r") as f:
    json_data = f.read()

# Convert the JSON data to a Python dictionary
data_list = json.loads(json_data)

# Manipulate the data as needed
print(data_list[0])
print(data_list[1])
