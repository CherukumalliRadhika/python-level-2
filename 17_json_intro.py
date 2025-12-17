import json

student = {
    "name": "Radhika",
    "age": 22,
    "skills": ["Python", "Git", "HTML"]
}

# Python dict -> JSON string
json_data = json.dumps(student, indent=4)
print("JSON string:")
print(json_data)

# JSON string -> Python dict
back_to_dict = json.loads(json_data)
print("Name from dict:", back_to_dict["name"])
