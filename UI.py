import imageio
from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path

video_name = str(Path().absolute()) + '/part1.mp4'
video = imageio.get_reader(video_name)
total_frames = int(video.get_meta_data()['duration'] * video.get_meta_data()['fps'])


def stream(label):
    try:
        image = video.get_next_data()
    except:
        video.close()
        return
    label.after(delay, lambda: stream(label))
    frame_image = ImageTk.PhotoImage(Image.fromarray(image))
    label.config(image=frame_image)
    label.image = frame_image


def image_video(seconds):
    global my_label

    image = video.get_data(int(seconds))
    frame_image = ImageTk.PhotoImage(Image.fromarray(image))

    my_label.config(image=frame_image)
    my_label.image = frame_image


if __name__ == '__main__':
    master = Tk()
    my_label = Label(master)
    my_label.pack()
    slider = Scale(master, from_=0, to=total_frames-1, orient=HORIZONTAL, command=image_video,
                   length=1000)
    slider.pack()
    button = Button(master, text="Initial", command=print(slider.get()))
    button.pack()

    master.mainloop()