import os
import json
import argparse
from collections import Counter


# Reads a JSON file and returns a list of dicts.
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
    # Parse command line args.
    parser = argparse.ArgumentParser()
    parser.add_argument("--json_corpus", help="JSON file with desired corpus.",
                        required=True)
    args = parser.parse_args()

    # Load the JSON file contents as a list of dicts.
    tracks_list = read_json_file(args.json_corpus)
    print(tracks_list[0]["track title"])

    # Perform word frequency analysis of track title.
    vocab_list = []
    for i, obj in enumerate(tracks_list):
        for word in obj["track title"].split(" "):
            vocab_list.append(word)
    print(vocab_list)
    word_freq = Counter(vocab_list)
    print(word_freq)

    # Make a X, Y dataset based on track title.

