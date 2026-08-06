from camera import Webcam

def main():
    camera = Webcam()
    camera.open()
    while camera.is_open():
        frame = camera.read_frame()
        if None:
            break


if __name__ == "__main__":
    main()