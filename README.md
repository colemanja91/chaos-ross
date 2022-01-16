# Chaos Ross

The Bob Ross Randomizer (**Chaos Ross**) generates episodes of _The Joy of Painting_, where each minute of the episode is randomly picked from different episodes.

You can use this for any set of input videos - the original use case of Bob Ross was just to introduce some happy little chaos to the world.

Example output: https://youtu.be/weabM5KyvsA

## Setup

_Recommended to use virtualenv for dependency management_

```sh
pip install -r requirements.txt
```

This depends heavily on the MoviePY library, and it's dependencies. 

## Source Videos

You'll need a set of _The Joy of Painting_ episodes to start with - the entire series is available for download on [the Internet Archive](https://archive.org/details/BobRossTheJoyOfPaintingS03). For best results, download at least one full season, and place them in a directory named `source_videos`.

To randomly get a set of videos from the first five seasons, you can run the following script:

```sh
python3 get_bob.py
```

This will download 13 (approx. 1 season) videos to the `source_videos` directory. 

(The count of videos downloaded is configurable via the `MAX_EPISODES` parameter within the `get_bob.py` script).

## Configuration

The following parameters are available for configuration within `main.py`:

* `INTERVAL`
  + Determines how many seconds of content are pulled from each source video
  + Recommended default: 15
* `FILENAME`
  + Set an output filename; default is a Heroku-style name

## Running

Basic usage: 

```sh
python3 main.py
```

The resulting video is written to a movie file in `output/` (full name will be displayed in the results). Additionally, a "spoiler log" will be generated, detailing which episodes were pulled from and in what order.
