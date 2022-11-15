import os
from moviepy.config import get_setting
from moviepy.tools import subprocess_call

NO_OP_FOLDER = 'No_Openning'


def ffmpeg_extract_subclip(filename, t1, t2, targetname):

    new_dir = os.path.join(os.path.dirname(filename), NO_OP_FOLDER)
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)

    cmd = [get_setting("FFMPEG_BINARY"), "-y",
           "-ss", "%0.2f" % t1,
           "-i", filename,
           "-t", "%0.2f" % (t2 - t1),
           "-c", "copy", targetname]

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
               "copy", targetname, '-y']
        subprocess_call(cmd)

    finally:
        os.remove(temp.name)


def cuttoff_clip(video, t1, t2):
    temp1 = video.raw_name + '_1' + video.extension
    temp2 = video.raw_name + '_2' + video.extension

    if t1 == 0:
        ffmpeg_extract_subclip(video.path, t2, t2 - 1, targetname=video.new_path)

    ffmpeg_extract_subclip(video.path, 0, t1, targetname=temp1)
    ffmpeg_extract_subclip(video.path, t2, video.duration, targetname=temp2)
    ffmpeg_concatenate_subclips(temp1, temp2, video.new_path)

    os.remove(temp1)
    os.remove(temp2)
