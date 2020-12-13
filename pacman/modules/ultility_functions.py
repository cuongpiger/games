from json import dump, load

def write_json_file(path, data):
    with open(path, 'w') as writer:
        dump(data, writer)


def read_json_file(path):
    try:
        with open(path) as reader:
            return load(reader)
    except:
        return None
