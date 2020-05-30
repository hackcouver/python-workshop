import ast
import pickle
import json

import pandas as pd
from tqdm import tqdm

'''
Were going to use Python dictionaries, which actually is not optimized but is simple to explain.
Essentiall were going to store the models as dictionaries of dictionaries.
'''

def getData() -> pd.Series:
    srs = pd.read_csv('data/tokenized.txt')['0']
    srs = srs.apply(lambda s: ast.literal_eval(s))
    return srs

def train(srs: pd.Series, verbose: bool = True) -> dict:
    # HERE ITS MORE EFFICIENT TO USE COUNTERS AND DEFAULTDICT, BUT ID RATHER NOT TEACH THAT
    model = {}

    if verbose:
        iterator = tqdm(srs.iteritems()) # adds a loadbar
    else:
        iterator = srs.iteritems()

    for index, value in iterator: # through the rows
        prev_token = value[0] # start token
        for token in value[1:]:
            if prev_token not in model:
                model[prev_token] = {}
            if token not in model[prev_token]:
                model[prev_token][token] = 1
            else:
                model[prev_token][token] += 1
            prev_token = token
    return model

if __name__ == "__main__":
    srs = getData()
    model = train(srs)
    # print(model)
    with open("data/model.json", "w") as f:
        f.write(json.dumps(model))
    
