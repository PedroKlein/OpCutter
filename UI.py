import os
import Cutter
from Video import Video
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image


video = None
master = Tk()
frame_samples = [0] * 2


def display_video(time):
    global video_label, video

    if not video:
        return

    image = video.file.get_data(int(time * video.fps))
    frame_image = ImageTk.PhotoImage(Image.fromarray(image))

    video_label.config(image=frame_image)
    video_label.image = frame_image


def open_dialog():
    global video, slider, button_frame_sample_0, button_frame_sample_1

    master.filename = filedialog.askopenfilename(title='Select a sample video')

    if not master.filename:
        print('cancel')
        return

    video = Video(master.filename)

    frame_samples[1] = video.duration

    display_video(0)

    button_frame_sample_0.config(state=NORMAL)
    button_frame_sample_1.config(state=NORMAL)
    slider.config(to=video.duration, state=ACTIVE)


def get_first_sample():
    global slider

    current_frame = int(slider.get())

    if current_frame >= frame_samples[1]:
        messagebox.showwarning("Warning", "First frame sample can't be bigger than Last frame sample")
        return

    frame_samples[0] = current_frame
    print(frame_samples)


def get_last_sample():
    global slider

    current_frame = int(slider.get())

    if frame_samples[0] >= current_frame:
        messagebox.showwarning("Warning", "Last frame sample can't be lower than the First frame sample")
        return

    frame_samples[1] = current_frame
    print(frame_samples)


def cut_op():
    global video

    Cutter.ffmpeg_extract_subclip(video.path, frame_samples[0], frame_samples[1], 'test.mp4')


if __name__ == '__main__':
    video_label = Label(master)
    video_label.pack()

    slider = Scale(master, from_=0, to=0, orient=HORIZONTAL, command=display_video,
                   length=1000, showvalue=0, state=DISABLED, takefocus=1)
    slider.pack()

    button_file = Button(master, text="Choose sample", command=open_dialog).pack()
    button_frame_sample_0 = Button(master, text="First frame sample", command=get_first_sample,
                                   state=DISABLED)
    button_frame_sample_0.pack()
    button_frame_sample_1 = Button(master, text="Second frame sample", command=get_last_sample,
                                   state=DISABLED)
    button_frame_sample_1.pack()

    button_cut = Button(master, text="Cut", command=cut_op)
    button_cut.pack()
    master.mainloop()
