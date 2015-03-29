import cv2

img = cv2.imread("tmp/jj.jpg")
height, width, depth = img.shape
density = float("{0:.2f}".format(680.0/width))
print density

img = cv2.resize(img, (0,0), fx=density, fy=density) 

cv2.imwrite('stella_sift_keypoints.jpg',img)

print height
print width
