import calc_des as calc_des
import os as os

print os.listdir("images")

for f in os.listdir("images"):
	kp, des = calc_des.calculate_sift("images/"+f)
	print des