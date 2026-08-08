from camera import Webcam
import cv2 as cv

class CloseWindow():
    def close(self):
        camera = Webcam()
        if camera.is_open:
            cv.VideoCapture(0).release()
            cv.destroyAllWindows()
        camera._is_open = False
