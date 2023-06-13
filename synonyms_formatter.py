import json
import os

with open("data/synonyms.json", "r") as f:
    data = f.read().split("\n")

    for i in range(len(data)):
        data[i] = json.loads(data[i])

    current_char = ""
    current_char_data = []

    new_data = []

    for i in range(len(data)):
        char = data[i]["word"][0].lower()

        if current_char == "":
            current_char = char
            current_char_data.append(data[i])
        elif current_char == char:
            current_char_data.append(data[i])
        else:
            new_data.append({"char": current_char, "data": current_char_data})
            current_char = char
            current_char_data = [data[i]]

    new_data.append({"char": current_char, "data": current_char_data})

    for i in range(len(new_data)):
        if not os.path.exists("data/synonyms/" + new_data[i]["char"]):
            os.mkdir("data/synonyms/" + new_data[i]["char"])
            with open("data/synonyms/" + new_data[i]["char"] + "/data.json", "w") as file:
                file.write(json.dumps(new_data[i]["data"]))
        else:
            old_data = []
            with open("data/synonyms/" + new_data[i]["char"] + "/data.json", "r") as file:
                old_data = json.loads(file.read())

            for j in range(len(new_data[i]["data"])):
                old_data.append(new_data[i]["data"][j])

            with open("data/synonyms/" + new_data[i]["char"] + "/data.json", "w") as file:
                file.write(json.dumps(old_data, indent=4))

