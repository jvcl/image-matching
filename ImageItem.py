import cv2
import numpy as np

class ImageItem:
	def __init__(self, image, image_name):
		# Instance variables
		self.key_points = []
		self.descriptor = []
		self.image = image
		self.image_name = image_name
		self.calculate()

	def key_points_and_descriptors(self):
		return (self.key_points, self.descriptor)

	def calculate(self):
		# detect keypoints in the image
		img = cv2.imread(self.image)
		#Resize umage if to big
		height, width, depth = img.shape
		print width
		print height
		if width > 680:
			height, width, depth = img.shape
			density = float("{0:.2f}".format(680.0/width))
			img = cv2.resize(img, (0,0), fx=density, fy=density)
		gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		sift = cv2.SIFT()
		self.key_points, self.descriptor = sift.detectAndCompute(gray,None)
		self.key_points = np.float32([kp.pt for kp in self.key_points])

	def name(self):
		return self.image_name
