from camera import Webcam
import cv2 as cv

class CloseWindow:
    def close(self, active_camera):
        if active_camera.is_open():
            cv.destroyAllWindows()
