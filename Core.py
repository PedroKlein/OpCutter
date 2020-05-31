from Video import Video
import Analyzer
import Cutter


def execute(op_video, target_video):
    target_video.first_op_frame = Analyzer.seek_first_frame(op_video, target_video)
    if Analyzer.confirm_op(op_video, target_video):
        # TODO: confirm last op frame
        target_video.first_op_frame = Analyzer.confirm_frame_in_video_backwards(target_video,
                                                                                target_video.first_op_frame)
        op_init_time_pos = target_video.first_op_frame / target_video.fps
        op_final_time_pos = op_video.duration + op_init_time_pos
        Cutter.cuttoff_clip(target_video, op_init_time_pos, op_final_time_pos)
        print(op_init_time_pos, op_final_time_pos)


execute(Video('op.mp4'), Video('D:\Series-filmes\Westworld S2\Westworld.S02E07.MP4.LEG.BaixarSeriesMP4.Com.mp4'))
