import os
import sys
import cv2
import numpy as np

print("OpenCV version:", cv2.__version__)
print("Current working directory:", os.getcwd())
print(sys.executable)
# conda: /Users/charliekillian/anaconda3/bin/python



class Aruco():
    def __init__(self, camera_calibration_parameters, dict):
        self.cv_file = cv2.FileStorage(camera_calibration_parameters, cv2.FILE_STORAGE_READ)
        self.mtx = self.cv_file.getNode('K').mat()
        self.dist = self.cv_file.getNode('D').mat()
        self.cv_file.release()
        self.aruco_dictionary = cv2.aruco.getPredefinedDictionary(dict)
        self.aruco_parameters = cv2.aruco.DetectorParameters()

    def get_aruco_dictionary(self, dict):
        return cv2.aruco.Dictionary_get(dict)

    def detect(self, frame):
        # (corners, marker_ids, rejected) = cv2.aruco.detectMarkers(
        #     frame, self.aruco_dictionary, parameters=self.aruco_parameters,
        #     cameraMatrix=self.mtx, distCoefs=self.dist)
        
        corners, marker_ids, rejected = cv2.aruco.detectMarkers(frame, self.aruco_dictionary, parameters=self.aruco_parameters)

        if corners:
            aruco_perimeter = cv2.arcLength(corners[0][0], True) #added 4-28-22 by CK
            print("ARC LENGTH: ", aruco_perimeter)
            print("Corners: ", corners)
            # calculate_distance(aruco_perimeter, 12)
            focal_length = 12
            pixel_height = aruco_perimeter
            distance_mm = (focal_length * 50 * 1080) / (pixel_height*11)
            distance_cm = distance_mm / 10
            print("Distance: ", distance_cm)
        
        if marker_ids is not None:

      # Draw a square around detected markers in the video frame
    
            cv2.aruco.drawDetectedMarkers(frame, corners, marker_ids)
            print("Marker ID: ", marker_ids)

        # Get the rotation and translation vectors
        # print('test1')
            rvecs, tvecs, obj_points = cv2.aruco.estimatePoseSingleMarkers(
            corners,
            self.aruco_marker_side_length,
            self.mtx,
            self.dist)
            

    def start_webcam(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            self.detect(frame)  # Call the detect method here
            cv2.imshow('Input', frame)

            c = cv2.waitKey(1)
            if c == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    dict = cv2.aruco.DICT_4X4_50
    # calibration_parameters_path = 'calibration_chessboard.yaml'
    calibration_parameters_path = 'calibration_chessboard.yaml'

    arUco = Aruco(calibration_parameters_path, dict)
    arUco.start_webcam()
    