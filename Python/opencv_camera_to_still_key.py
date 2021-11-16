## https://note.nkmk.me/python-opencv-camera-to-still-image/

import cv2
import os

def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    ret, frame = cap.read()
    cv2.imshow(window_name, frame)

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    n = 0
    while True:
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('c'):
            cv2.imshow(window_name, frame)
            print('{}_{}.{}'.format(base_path, n, ext))
            cv2.imwrite('{}_{}.{}'.format(base_path, n, ext), frame)
            n += 1
        elif key == ord('q'):
            break

    cv2.destroyWindow(window_name)


save_frame_camera_key(0, 'data/temp', 'camera_capture')
