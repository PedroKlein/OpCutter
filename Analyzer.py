import cv2
import numpy as np

def compare_with_sample(sample_path, video_path):
    sample = cv2.VideoCapture(sample_path)
    video = cv2.VideoCapture(video_path)
    img = cv2.imread('frame20sec.jpg')

    while sample.isOpened():
        ret, frame = sample.read()
        if not np.any(cv2.subtract(img, frame)):
            print('OK')
    # while video.isOpened():
    #     ret, frame = video.read()
    #     while sample.isOpened():
    #         ret_sample, frame_sample = sample.read()
    #         score, diff = compare_ssim(grayA, grayB, full=True)
    #         diff = (diff * 255).astype("uint8")
    #         print("SSIM: {}".format(score)

    sample.release()
    video.release()

compare_with_sample('test.mp4', 'test.mp4')

# vidcap = cv2.VideoCapture('test.mp4')
# vidcap.set(cv2.CAP_PROP_POS_MSEC,20000)      # just cue to 20 sec. position
# success, image = vidcap.read()
# if success:
#     cv2.imwrite("frame20sec.jpg", image)     # save frame as JPEG file
#     cv2.imshow("20sec",image)
#     cv2.waitKey()