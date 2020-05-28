import os
import imageio
from moviepy.config import get_setting
from moviepy.tools import subprocess_call

NO_OP_FOLDER = 'No_Openning'


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
               "copy", targetname, '-y']
        subprocess_call(cmd)

    finally:
        os.remove(temp.name)


def cuttoff_clip(file, t1, t2):

    video = imageio.get_reader(file)
    video_duration = video.get_meta_data()['duration']

    filename = os.path.basename(file)
    name, extension = os.path.splitext(filename)

    new_file_path = os.path.join(os.path.dirname(file), NO_OP_FOLDER, filename)

    temp1 = name + '_1' + extension
    temp2 = name + '_2' + extension

    if t1 == 0:
        ffmpeg_extract_subclip(file, t2, video_duration, targetname=new_file_path)

    ffmpeg_extract_subclip(file, t2, video_duration, targetname=temp2)
    ffmpeg_extract_subclip(file, 0, t1, targetname=temp1)
    ffmpeg_concatenate_subclips(temp1, temp2, new_file_path)

    os.remove(temp1)
    os.remove(temp2)

