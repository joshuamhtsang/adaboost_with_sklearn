import os
import json


def read_json_file(filename):
    objs = []

    with open(filename, 'r') as file_handle:
        for line in file_handle:
            print(line)
            try:
                objs.append(json.loads(line))
            except json.decoder.JSONDecodeError:
                pass

    return objs


if __name__ == '__main__':
    tracks_list = read_json_file('small.json')

    print(tracks_list[0]["track title"])
