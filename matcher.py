
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
		return result

	def get_score(self, query_kps, query_descriptor, kps, descriptor):
		"""
		Method to score the similarity of the query image with another image
		"""
		matcher = cv2.DescriptorMatcher_create("BruteForce")
		rawMatches = matcher.knnMatch(descriptor, query_descriptor, 2)
		matches = []

		return 1

