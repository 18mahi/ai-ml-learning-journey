import json
File_NAME = 'tasks.json'
def load_tasks():
    try:
        with open(File_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open(File_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)
    
