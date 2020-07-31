import json
from difflib import get_close_matches

with open("/Users/winsorhoang/dev/python/projects/dictionary/dictionary.json") as f:
    data = json.load(f)


def interface(user_word):
    user_word = user_word.lower()
    if user_word in data:
        return data[user_word]
    elif len(get_close_matches(user_word, data.keys())) > 0:
        yes_no = input(
            "Did you mean %s instead? Y/N  "
            % get_close_matches(user_word, data.keys())[0]
        ).lower()
        if yes_no == "n":
            return "No word found!"
        elif yes_no == "y":
            return data[get_close_matches(user_word, data.keys())[0]]

    return None


user_word = input("Enter your query: ")
output = interface(user_word)


if output != "No word found!":
    for item in output:
        print(item, end="")
else:
    print(output)
