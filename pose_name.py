import cv2


class OpenPose():
	"""docstring for OpenPose"""
	def __init__(self, show_name, show_prob):
		self.show_name = show_name
		self.show_prob = show_prob
	
	# the format of img is OpenCv	
	def mountain(self, img):
		self.show_name.setText('Mountain Pose')
		self.show_prob.setText('1000%')
		

		cv2.imshow("Img", img)
		cv2.waitKey()
		cv2.destroyAllWindows()
		pass

	def side(self, img):
		pass

	def warrior(self, img):
		pass

	def seat_one(self, img):
		pass

	def seta_two(self, img):
		pass