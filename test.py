from ImageItem import ImageItem
import os as os
import matcher as matcher
import time


#print os.listdir("images")

list_images = []

start2 = time.clock()
for f in os.listdir("images"):
	image = ImageItem("images/"+f, f)
	list_images.append(image)

matcher = matcher.Matcher()

elap2 = time.clock() - start2

print elap2
for f in os.listdir("queries"):
	start2 = time.clock()
	query = ImageItem("queries/"+f, f)
	r = {}
	r = matcher.search(query, list_images)
	elap2 = time.clock() - start2
	print r, elap2


