import cv2 as cv
from camera import Webcam

class FrameCapture:
    def capture_frame(self, get_frame):
        filename = "userinput.jpg"
        cv.imwrite(filename, get_frame)
