#include "aruco/markerdetector.h"
#include <opencv2/flann.hpp>
using namespace std;

int main(int argc char ** argv)
{
  cv::VideoCapture vcap;
  aruco::MarkerDetector Mdetector;
  Mdetector.setDirectionMode(aruco::DM_VIDEO_FAST);
  cv::Mat InImage;

  vcap.open(argv[1]);
  while(vcap.grab())
  {
    vcap.retrieve(InImage);

    vector<aruco::Marker> Markers = MDetector.detect(InImage);
    for (unsigned int i = 0; i < Markers.size(); i++)
    {
      cout << Markers[i] << endl;
      Markers[i].draw(InImage, cv::Scalar(0,0,225),2);
    }

    cv::namedWindow("in", 1);
    cv::imshow("in", InImage);
    while (char(cv::waitKey(0) != 27)
      ;
  }
}
