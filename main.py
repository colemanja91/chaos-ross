#!/usr/bin/python3

from random import randint
from glob import glob
from json import dump
from moviepy.editor import VideoFileClip, concatenate_videoclips
from haikunator import Haikunator

# CONFIG
INTERVAL = 15  # Seconds for each segment
FILENAME = Haikunator().haikunate()

# Constants
SPOILER_LOG = []
SOURCE_VIDEOS = glob("./source_videos/*.avi")


def log(filename, start, end):
  # Add clip to spoiler log
    SPOILER_LOG.append({
        "filename": filename,
        "start": start,
        "end": end
    })


def next_clip(start, end):
  # Next clip to be appended
    filename = SOURCE_VIDEOS[randint(0, len(SOURCE_VIDEOS)-1)]
    clip = VideoFileClip(filename)

    final_end = end
    has_more = True
    duration = clip.duration

    if start > duration:
        return None, False

    if end > duration:
        final_end = duration
        has_more = False

    log(filename, start, final_end)

    return clip.subclip(start, final_end), has_more


def create_video():
  # Generate random episode
    filename = FILENAME

    clips = []
    start = 0
    interval = INTERVAL
    has_more = True

    while has_more:
        add_clip, has_more = next_clip(start, start + interval)
        start += interval
        if add_clip:
            clips.append(add_clip)

    # concat and write
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(f"output/{filename}.mp4")
    print("New episode generated!\n")
    print(f"Filename: {filename}")

    # write log
    with open(f"output/{filename}_LOG.json", "w") as fopen:
        dump(SPOILER_LOG, fopen)


if __name__ == "__main__":
    create_video()
