import os
import imageio

NO_OP_FOLDER = 'No_Openning'


class Video:

    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.raw_name, self.extension = os.path.splitext(self.name)
        self.new_path = os.path.join(os.path.dirname(path), NO_OP_FOLDER, self.name)
        self.file = imageio.get_reader(path)

        self.first_op_frame = 0
        self.fps = self.file.get_meta_data()['fps']
        self.duration = self.file.get_meta_data()['duration']

    @property
    def total_frames(self):
        return int(self.duration * self.fps)
