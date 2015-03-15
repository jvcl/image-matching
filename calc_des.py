import cv2
import numpy as np

def calculate_sift(name):
	#Read the image
    img = cv2.imread(name)
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#load sift
    sift = cv2.SIFT()
     #Detect the KeyPoints descriptors
    kp, des = sift.detectAndCompute(gray,None)
    return kp, des
