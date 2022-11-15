import cv2

FRAME_OFFSET = 100
MINIMUM_HIST_DIFF = 3790
ENOUGH_SCORE = MINIMUM_HIST_DIFF * 10


def seek_first_frame(op_video, target_video):
    video = cv2.VideoCapture(target_video.path)
    video_sample = cv2.VideoCapture(op_video.path)

    video_sample.set(cv2.CAP_PROP_POS_FRAMES, 0)

    result = seek_frame_in_video(video_sample.read()[1], video)

    video.release()
    video_sample.release()

    return result


def confirm_op(op_video, target_video):
    video = cv2.VideoCapture(target_video.path)
    video_sample = cv2.VideoCapture(op_video.path)

    video.set(cv2.CAP_PROP_POS_FRAMES, target_video.first_op_frame + FRAME_OFFSET)

    score = 0
    for i in range(int(target_video.fps)):

        frame_vid = video.read()[1]
        video_sample.set(cv2.CAP_PROP_POS_FRAMES, FRAME_OFFSET)

        for j in range(int(target_video.fps)):
            frame_sample = video_sample.read()[1]
            img_hist_diff = hist_compare(frame_vid, frame_sample)
            if img_hist_diff >= MINIMUM_HIST_DIFF:
                score += hist_compare(frame_vid, frame_sample)
            if score >= ENOUGH_SCORE:
                print('Confirmed')
                return True

    print('Not Confirmed')
    return False


def seek_frame_in_video(frame_sample, video, start_frame=0):
    video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    while video.isOpened():
        frame_vid = video.read()[1]
        img_hist_diff = hist_compare(frame_vid, frame_sample)
        if img_hist_diff >= MINIMUM_HIST_DIFF:
            print('Matched')
            return video.get(cv2.CAP_PROP_POS_FRAMES)

        elif img_hist_diff == 0:
            print('End')
            return None


def confirm_frame_in_video_backwards(target_video, start_frame=-1):

    video = cv2.VideoCapture(target_video.path)
    video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    frame_sample = video.read()[1]

    new_first_frame = start_frame

    while video.isOpened():
        video.set(cv2.CAP_PROP_POS_FRAMES, video.get(cv2.CAP_PROP_POS_FRAMES) - 2)
        frame_vid = video.read()[1]

        img_hist_diff = hist_compare(frame_vid, frame_sample)
        if img_hist_diff >= MINIMUM_HIST_DIFF - 1000:
            print('Found One')
            new_first_frame = video.get(cv2.CAP_PROP_POS_FRAMES)
        else:
            print('End')
            return new_first_frame


def hist_compare(image1, image2):
    image1_hist = cv2.calcHist([image1], [0], None, [256], [0, 256])
    image2_hist = cv2.calcHist([image2], [0], None, [256], [0, 256])
    test = cv2.compareHist(image1_hist, image2_hist, cv2.HISTCMP_INTERSECT) / 100
    return test
