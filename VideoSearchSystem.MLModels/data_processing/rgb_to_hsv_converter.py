import cv2

class RGBToHSVConverter:
    @staticmethod
    def convert(frame):
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        return hsv_frame
