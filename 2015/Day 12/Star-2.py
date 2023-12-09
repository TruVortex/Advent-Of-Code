from json import loads


def process(data):
    if isinstance(data, str):
        return 0
    if isinstance(data, int):
        return data
    if isinstance(data, list):
        return sum([process(subdata) for subdata in data])
    return ('red' not in data.values()) and process(list(data.values()))


print(process(loads(open('input', 'r').read())))
