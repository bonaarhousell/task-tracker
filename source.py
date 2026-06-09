import json

def load_json():
    with open("tasks.json", "r") as file:
        return json.load(file)

def dump_json(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)