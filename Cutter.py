import os
import subprocess as sp
import sys

from moviepy.config import get_setting
from moviepy.tools import subprocess_call


def ffmpeg_extract_subclip(filename, t1, t2, targetname):

    cmd = [get_setting("FFMPEG_BINARY"), "-y",
           "-ss", "%0.2f" % t1,
           "-i", filename,
           "-t", "%0.2f" % (t2 - t1),
           "-map", "0", "-vcodec", "copy", "-acodec", "copy", targetname]

    subprocess_call(cmd)

def ffmpeg_concatenate_subclips(file1, file2, targetname):

    temp = open("temp.txt", "w+")

    try:
        temp.writelines("file '" + os.path.abspath(file1) + "'\n")
        temp.writelines("file '" + os.path.abspath(file2) + "'")
        temp.close()

        cmd = [get_setting("FFMPEG_BINARY"), "-safe",
               "0", "-f",
               "concat", "-i",
               os.path.abspath(temp.name), "-c",
               "copy", targetname]
        subprocess_call(cmd)

    finally:
        os.remove(temp.name)

def cuttoff_clip(file, t1, t2):
    temp1 = 'part1.mp4'
    temp2 = 'part2.mp4'

    ffmpeg_extract_subclip(file, 0, t1, targetname=temp1)
    ffmpeg_extract_subclip(file, t2, 1000, targetname=temp2)
    ffmpeg_concatenate_subclips(temp1, temp2, os.path.abspath('test.mp4'))

cuttoff_clip("D:\Series-filmes\Westworld S2\Westworld.S02E03.mp4", 5, 400)

