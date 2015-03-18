import cv2
import numpy as np

class ImageItem:
	def __init__(self, image):
		# Instance variables
		self.key_points = []
		self.descriptor = []
		self.image = image

	def key_points_and_descriptors(self):
		return (self.key_points, self.descriptor)
	
	def calculate(self):
		# detect keypoints in the image
		img = cv2.imread(self.image)
		gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		sift = cv2.SIFT()
		self.key_points, self.descriptor = sift.detectAndCompute(gray,None)
		self.key_points = np.float32([kp.pt for kp in self.key_points])
