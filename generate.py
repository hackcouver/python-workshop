import json
import random


def generate(model: dict) -> str:
    token = '__START__'
    s = ''
    while True:
        if token is not '__START__':
            s += token + ' '
        choices = tuple(model[token].keys())
        weights = tuple(model[token].values())
        next_token = random.choices(choices, weights=weights)[0]
        if next_token == "__END__":
            break
        token = next_token
    return s

if __name__ == "__main__":
    with open("data/model.json", "r") as f:
        model = json.load(f)
    for _ in range(10):
        print(generate(model))