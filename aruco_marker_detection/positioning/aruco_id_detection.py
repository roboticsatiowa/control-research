from __future__ import print_function # Python 2/3 compatibility
import cv2 # Import the OpenCV library
# import numpy as np # Import Numpy library
# from scipy.spatial.transform import Rotation as R
# import math # Math library
# from argparse import ArgumentParser #added by CK by 4-28-22 while debugging 'argparse not defined'
import pyautogui

ARUCO_DICT = {
    "DICT_4X4_50": cv2.aruco.DICT_4X4_50
}
# Side length of the ArUco marker in meters
aruco_marker_side_length = 0.0500

# Calibration parameters yaml file
camera_calibration_parameters_filename = 'calibration_chessboard.yaml'

def screenshot():
  myScreenshot = pyautogui.screenshot()
  myScreenshot.save(r'Desktop \ aruco.png')

def main():
  """
  Main method of the program.
  """
  # Check that we have a valid ArUco marker
  # if ARUCO_DICT.get(aruco_dictionary_name, None) is None:
  #   print("[INFO] ArUCo tag of '{}' is not supported".format(
  #     args["type"]))
  #   sys.exit(0)

  # Load the camera parameters from the saved file
  cv_file = cv2.FileStorage(
    camera_calibration_parameters_filename, cv2.FILE_STORAGE_READ)
  mtx = cv_file.getNode('K').mat()
  dst = cv_file.getNode('D').mat()
  cv_file.release()

  # Load the ArUco dictionary
  print("[INFO] detecting '{}' markers...".format(
    'DICT_4x4_50'))
  this_aruco_dictionary = cv2.aruco.Dictionary_get(ARUCO_DICT["DICT_4X4_50"]) # Changed to working dictionary, formerly aruco_dictionary_name
  this_aruco_parameters = cv2.aruco.DetectorParameters_create()

  # Start the video stream
  cap = cv2.VideoCapture(0)

  while(True):

    # Capture frame-by-frame
    # This method returns True/False as well
    # as the video frame.
    ret, frame = cap.read()

    # Detect ArUco markers in the video frame
    (corners, marker_ids, rejected) = cv2.aruco.detectMarkers(
      frame, this_aruco_dictionary, parameters=this_aruco_parameters,
      cameraMatrix=mtx, distCoeff=dst)


    # Check that at least one ArUco marker was detected
    if marker_ids is not None:

      # Draw a square around detected markers in the video frame
    
      cv2.aruco.drawDetectedMarkers(frame, corners, marker_ids)
      print("Marker ID: ", marker_ids)

      # Get the rotation and translation vectors
      # print('test1')
      rvecs, tvecs, obj_points = cv2.aruco.estimatePoseSingleMarkers(
        corners,
        aruco_marker_side_length,
        mtx,
        dst)

      # take screenshot of marker
      screenshot()

    # Display the resulting frame
    cv2.imshow('frame',frame)

    # If "q" is pressed on the keyboard,
    # exit this loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # Close down the video stream
  cap.release()
  cv2.destroyAllWindows()




if __name__ == '__main__':
  print(__doc__)
  main()
