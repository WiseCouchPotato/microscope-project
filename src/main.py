from camera import Webcam
from display import OpenWindow
import cv2 as cv
from display.close_window import CloseWindow


def main():
    """instantiate camera and display class in main"""
    camera = Webcam()
    display = OpenWindow()
    stop_display = CloseWindow()


    """open camera and capture frame while true"""
    camera.open()
    if not camera.is_open():
        print("cannot get video stream")
    else:
        print("success")
    while camera.is_open():
        frame = camera.read_frame()
        if frame is None:
            break
        if display.display_window(frame):
            break
    camera.close()
    stop_display.close()
    """display frame while previous is true"""


if __name__ == "__main__":
    main()