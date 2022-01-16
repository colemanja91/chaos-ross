#!/usr/bin/python

import os
from random import randint
from json import load

# CONFIG
MAX_EPISODES = 13

with open("tjop_manifest.json", "r") as fopen:
    SOURCE_EPISODES = load(fopen)["episodes"]


def run():
    i = 1

    while 1 < MAX_EPISODES:
        index = randint(0, len(SOURCE_EPISODES))
        episode = SOURCE_EPISODES[index]
        url = episode["url"]

        os.system(f"wget -nc {url} ./source_videos/")

        del SOURCE_EPISODES[index]


if __name__ == "__main__":

    run()
