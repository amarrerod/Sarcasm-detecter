#!/usr/bin/python3

import json
import pandas as pd
from urllib.parse import urlparse


FILENAME = "Sarcasm_Headlines_Dataset.json"


def parse_data(file):
    for l in open(file, 'r'):
        yield json.loads(l)


def extract_source(entry):
    # Extraemos el diario del articulo
    return urlparse(entry).netloc


if __name__ == "__main__":
    data = pd.read_json(FILENAME, lines=True)
    # Nos quedamos solo con la base de la URL
    data["article_link"] = data["article_link"].apply(extract_source)
    y = data["is_sarcastic"]
    X = data.loc[:, data.columns != "is_sarcastic"]
    print(f"X: \n{X}")
