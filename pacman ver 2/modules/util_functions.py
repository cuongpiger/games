from json import load


def readJson(path):
    try:
        with open(path) as rd:
            return load(rd)
    except:
        return None
