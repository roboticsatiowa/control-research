from __future__ import print_function # Python 2/3 compatibility
import cv2 # Import the OpenCV library
import numpy as np # Import Numpy library
# from scipy.spatial.transform import Rotation as R
# import math # Math library
# from argparse import ArgumentParser #added by CK by 4-28-22 while debugging 'argparse not defined'
import pyautogui
# Side length of the ArUco marker in meters
aruco_dictionary_name = "DICT_ARUCO_ORIGINAL"
ARUCO_DICT = {
    "DICT_4X4_50": cv2.aruco.DICT_4X4_50
}
aruco_marker_side_length = 0.0500

# Calibration parameters yaml file
camera_calibration_parameters_filename = 'calibration_chessboard.yaml'
def screenshot(marker_ids):
  myScreenshot = pyautogui.screenshot()
  filename = "Marker ID: "+ str(marker_ids) + '.png'
  print('running')
  myScreenshot.save(filename)

def main():
  
#Setting up screen recording

# Specify resolution
  resolution = tuple(pyautogui.size())
  
# Specify video codec
  codec = cv2.VideoWriter_fourcc(*"XVID")
  
# Specify name of Output file
  #filename = "Recording.mov"
  
# Specify frames rate. We can choose any 
# value and experiment with it
  fps = 1
  
  
# Creating a VideoWriter object
  # out = cv2.VideoWriter(filename, codec, fps, resolution)
  
# Create an Empty window
  cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
  
# Resize this window
  cv2.resizeWindow("Live", 480, 270)
  cv_file = cv2.FileStorage(
    camera_calibration_parameters_filename, cv2.FILE_STORAGE_READ)
  mtx = cv_file.getNode('K').mat()
  dst = cv_file.getNode('D').mat()
  this_aruco_dictionary = cv2.aruco.Dictionary_get(ARUCO_DICT["DICT_4X4_50"]) # Changed to working dictionary, formerly aruco_dictionary_name
  this_aruco_parameters = cv2.aruco.DetectorParameters_create()

  while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()
  
    # Convert the screenshot to a numpy array
    frame = np.array(img)
  
    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    (corners, marker_ids, rejected) = cv2.aruco.detectMarkers(
      frame, this_aruco_dictionary, parameters=this_aruco_parameters,
      cameraMatrix=mtx, distCoeff=dst)
    if marker_ids is not None:
      print("Marker ID: ", marker_ids)
      cv2.imwrite("Marker_ID_"+str(marker_ids)+".jpg", frame)
    # Write it to the output file
    #out.write(frame)
      
    # Optional: Display the recording screen
    #cv2.imshow('Live', frame)
      
    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break
  
# Release the Video writer
  out.release()
  
# Destroy all windows
  cv2.destroyAllWindows()
"""
  Main method of the program.
  """
  # Check that we have a valid ArUco marker
  # if ARUCO_DICT.get(aruco_dictionary_name, None) is None:
  #   print("[INFO] ArUCo tag of '{}' is not supported".format(
  #     args["type"]))
  #   sys.exit(0)

  # Load the camera parameters from the saved file
'''
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
      print("Marker ID: ", marker_ids)

    # Display the resulting frame
    #cv2.imshow('frame',frame)

    screenshot(marker_ids)
'''
  





if __name__ == '__main__':
  print(__doc__)
  main()
