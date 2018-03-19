import json

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

with open('numbers.json', 'w') as file_object:
    json.dump(numbers, file_object)

profile = {
    "name": "Jacky",
    "age": 26,
    "address": "Sichuan,Chengdu"
}

with open('profile.json', 'w') as file_object:
    json.dump(profile, file_object)

# =================================================

with open('profile.json') as file_object:
    p = json.load(file_object)
    print(p["name"])