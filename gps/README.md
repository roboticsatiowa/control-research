# GPS

- [GPS data sheet](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-ultimate-gps.pdf)
- [ROS Diver](http://wiki.ros.org/nmea_navsat_driver)

### Connection:
| GPS | Jetson Nano |
|--|--|
|3.3 V | 3.3 V|
| GND | GND |
| TX | PIN 10 |
| RX | PIN 8 |

### Commands:

```
# install ROS driver
sudo apt install ros-melodic-nmea-navsat-driver

# temporarily allow r/w permissions to GPIO rx and tx pins on Jetson Nano
# more info: https://forums.developer.nvidia.com/t/read-write-permission-ttyths1/81623
sudo chmod 666 /dev/ttyTHS1

# run
rosrun nmea_navsat_driver nmea_serial_driver _port:/dev/ttyTHS1 _baud:=9600
```
