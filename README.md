# Chaos Ross

The Bob Ross Randomizer (**Chaos Ross**) generates episodes of _The Joy of Painting_, where each minute of the episode is randomly picked from different episodes.

## Setup

_Recommended to use virtualenv for dependency management_

```sh
pip install -r requirements.txt
```

This depends heavily on the MoviePY library, and it's dependencies. 

## Source Videos

You'll need a set of _The Joy of Painting_ episodes to start with - the entire series is available for download on [the Internet Archive](https://archive.org/details/BobRossTheJoyOfPaintingS03). For best results, download at least one full season, and place them in a directory named `source_videos`.

## Running

Basic usage: 

```sh
python3 main.py
```

The resulting video is written to a movie file in `output/` (full name will be displayed in the results). Additionally, a "spoiler log" will be generated, detailing which episodes were pulled from and in what order.
