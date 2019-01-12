import os
import json
import argparse


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
    parser = argparse.ArgumentParser()
    parser.add_argument("--json_corpus", help="JSON file with desired corpus.",
                        required=True)
    args = parser.parse_args()

    tracks_list = read_json_file(args.json_corpus)
    print(tracks_list[0]["track title"])

    # Make a X, Y dataset based on track title.
    vocab_track_title = set()
    for i, obj in enumerate(tracks_list):
        print(i, obj)
        for word in obj["track title"].split(" "):
            vocab_track_title.add(word)

    print(vocab_track_title)
