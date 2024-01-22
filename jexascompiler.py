import json
import os

json_file_path = 'mainfile.json'

with open(json_file_path, 'r') as file:
    json_data = file.read()

data = json.loads(json_data)

file_path = data['file']

with open(file_path, 'r') as file_content:
    content = file_content.read()

content = content.replace("//", "#")
content = content.replace("func", "def")
content = content.replace("write", "print")
content = content.replace("+-", "('")
content = content.replace("-+", "')")

exec(content)
