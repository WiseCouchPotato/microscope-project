import cv2 as cv

class Webcam:
    """Represents a webcam used by the microscope"""

    def __init__(self):
        self._is_open = False # starts at a initial condition of false
        self._capture = None # no capture stream

    def open(self):
        self._capture = cv.VideoCapture(0) # 0 stands for webcam stream
        self._is_open = self._capture.isOpened() # boolean check if open

    def read_frame(self):
        ret, frame = self._capture.read()
        if ret:
            return frame
        return None

    def is_open(self):
        return self._is_open