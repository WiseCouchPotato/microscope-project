import cv2 as cv
from camera import Webcam

camera = Webcam()

class OpenWindow:
    """Represents the window displayed when webcam is opened"""

    def display_window(self, frame):
        cv.imshow("Frame", frame)