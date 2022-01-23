import cv2
from cv2 import aruco
import matplotlib.pyplot as plt

aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

def main():
	name = "Live Video Feed"
	cv2.namedWindow(name)
	videoCapture = cv2.VideoCapture(0)

	if videoCapture.isOpened():
		ret, frame = videoCapture.read()
	else:
		ret = False

	while ret:
		ret, frame = videoCapture.read()
		output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow(name, frame)

		parameters =  aruco.DetectorParameters_create()
		corners, ids, rejectedImgPoints = aruco.detectMarkers(
			frame, 
			aruco_dict, 
			parameters=parameters)

		#frame_markers = aruco.drawDetectedMarkers(frame, corners, ids)
		#cv2.imshow(name, frame_markers)

		if ids is not None:
			#print(ids)
			for i in range(len(ids)):
				c = corners[i][0]
				#cv2.circle([c[:, 0].mean()], [c[:, 1].mean()], 20, (255, 0, 0), 2)
				cv2.circle(frame, [c[:, 1].mean()], 20, (255, 0, 0), 2)

		if cv2.waitKey(1) == 27:
			break

	cv2.destroyWindow(name)
	videoCapture.release()

main()
