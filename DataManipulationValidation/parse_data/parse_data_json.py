import json

file_path = "grocceries.json"

with open(file_path, "r") as file:
    data = file.read()

parsed_data = json.loads(data)
print("apples qty: ", parsed_data["apples"])