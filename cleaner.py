import nltk
import pandas as pd

nltk.download("punkt")


def getData() -> pd.Series:
    return pd.read_csv("data/trump.txt", sep="\n", header=None)[0]


def cleanData(srs: pd.Series) -> pd.Series:
    # remove intro
    srs = srs.str.slice(start=79)
    # strip whitespace
    srs = srs.str.strip()
    # remove strings too short
    srs = srs[srs.str.len() > 20]
    # remove links
    srs = srs[~srs.str.startswith("pic.twitter.com")]
    # remove elipses
    srs = srs.str.replace("....", "", regex=False)
    # remove tags
    srs = srs.str.replace("@[a-zA-Z]+ ", "")
    # remove links
    srs = srs.str.replace("[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", "")
    return srs


def tokenize(s: str) -> str:
    # tokenize
    results = nltk.word_tokenize(s)
    results = ["__START__"] + results + ["__END__"]
    return results


def tokenizeSeries(srs: pd.Series) -> pd.Series:
    return srs.apply(tokenize)


if __name__ == "__main__":
    srs = getData()
    srs = cleanData(srs)
    srs = tokenizeSeries(srs)
    srs = srs.reindex()
    print(srs.head(40))
    srs.to_csv("data/tokenized.txt")
