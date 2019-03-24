import cv2
import numpy as np
import math
from pynput.keyboard import Key,Controller

def stearingWheel():
    cap=cv2.VideoCapture(0)


    while True:
        ret,frame=cap.read()

        frame=cv2.line(frame,(100,400),(50,135),(45,44,45),10)
        cv2.imshow('none',frame)

        if cv2.waitKey(1)==27:
            break

    cap.release()
    cv2.destroyAllWindows()

def gameConnection():
    pass


if __name__ == "__main__":
    #stearingWheel();
    keyboard=Controller()z
    while True:
