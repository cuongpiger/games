from json import load
import hashlib


def readJson(path):
    try:
        with open(path) as rd:
            return load(rd)
    except:
        return None

def hashFunction(maze):
    return hashlib.sha1(maze.tobytes()).hexdigest()