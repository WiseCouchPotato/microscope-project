from camera import Webcam
from display import OpenWindow
import cv2 as cv
from display import CloseWindow
from capture import FrameCapture

def main():
    """instantiate camera and display class in main"""
    camera = Webcam()
    display = OpenWindow()
    stop_display = CloseWindow()
    capture_image = FrameCapture()

    """open camera and capture frame while true"""
    camera.open()
    while camera.is_open():
        frame = camera.read_frame()

        if frame is None:
            break
        display.display_window(frame)
        key = cv.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            capture_image.capture_frame(frame)


    stop_display.close()
    camera.close()
    """display frame while previous is true"""


if __name__ == "__main__":
    main()