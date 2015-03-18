from ImageItem import ImageItem
import os as os
import matcher as matcher

#print os.listdir("images")

list_images = []

for f in os.listdir("images"):
	image = ImageItem(f)
	list_images.append(image)

matcher = matcher.Matcher()

query = ImageItem("1.jpg")
matcher.search(query, list_images)