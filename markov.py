import pandas as pd
import numpy as np
from tqdm import tqdm

def getData() -> pd.Series:
	return pd.read_csv('data/tokenized.txt')[0]
