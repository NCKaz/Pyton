# TODO решите задачу
import json

file = "input.json"

def task() -> float:
    with open(file) as f:
        json_data = json.load(f)
        values = sum([i["score"] * i["weight"] for i in json_data])

    return round(values, 3)
print(task())
