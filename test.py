from ImageItem import ImageItem
import os as os

#print os.listdir("images")

for f in os.listdir("images"):
	image = ImageItem("images/"+f)
	(k, d) = image.key_points_and_descriptors()
	print d
