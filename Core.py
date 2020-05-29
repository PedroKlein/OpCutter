from Video import Video
import Analyzer


def nicole(op_video, target_video):
    target_video.first_op_frame = Analyzer.seek_first_frame(op_video, target_video)
    if Analyzer.confirm_op(op_video, target_video):
        op_init_time_pos = target_video.first_op_frame/target_video.fps
        op_final_time_pos = op_video.duration + op_init_time_pos
        print(op_init_time_pos, op_final_time_pos)




nicole(Video('op.mp4'), Video('D:\Series-filmes\Westworld S2\Westworld.S02E10.MP4.LEG.BaixarSeriesMP4.Com.mp4'))
