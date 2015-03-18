
import numpy as np
import cv2

class Matcher:
	
	def search(self, query_image, list_images):
		"""
		Method to search in the database a match with the query image
		"""
		result = {}
		# Get variables from query image
		query_kps, query_descriptor = query_image.key_points_and_descriptors()
		# Loop in the list of images
		for image in list_images:
			# Varuables of the current image
			kps, descriptor = image.key_points_and_descriptors()
			# Get the score of the current image compared with the query image
			score = self.get_score(query_kps, query_descriptor, kps, descriptor)
			result[image.name()] = score

		# Sort results by score
		if len(result) > 0:
			result = sorted([(v, k) for (k, v) in result.items() if v > 0],
				reverse = True)
		return result

	def get_score(self, query_kps, query_descriptor, kps, descriptor):
		"""
		Method to score the similarity of the query image with another image
		"""
		ratio = 0.7
		minMatches = 50
		matcher = cv2.DescriptorMatcher_create("BruteForce")
		rawMatches = matcher.knnMatch(descriptor, query_descriptor, 2)
		matches = []

		#Matching as per pyImageSearch

		for m in rawMatches:
			# ensure the distance is within the ratio in the paper of SIFT
			if len(m) == 2 and m[0].distance < m[1].distance * ratio:
				matches.append((m[0].trainIdx, m[0].queryIdx))
		if len(matches) > minMatches:
			# construct the two sets of points
			ptsA = np.float32([query_kps[i] for (i, _) in matches])
			ptsB = np.float32([kps[j] for (_, j) in matches])

			# compute the homography between the two sets of points
			# and compute the ratio of matched points
			(_, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, 4.0)

			# return the ratio of the number of matched keypoints
			# to the total number of keypoints
			return float(status.sum()) / status.size

		# no matches were found
		return -1.0
