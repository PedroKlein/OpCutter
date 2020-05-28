import cv2

# Opens the Video file
cap = cv2.VideoCapture('D:/Series-filmes/Anime_Monster_legendado_ptbr/Monster_01.rmvb')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
while cap.isOpened():
    ret, frame = cap.read()

    if ret is True:
        out.write(frame)


cap.release()
out.release()

cv2.destroyAllWindows()