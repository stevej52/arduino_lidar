# arduino_lidar
Arduino Circutpython code to run 3 adafruit_vl53l0x boards and send data string with 3 distances to serial. Tested on Adafruit Trinket M0 and Teensy 4.0

Running one vl53l0x with the adafruit example code is pretty easy but running 2 or more is harder because you have to reset each one and set the I2C address. It loses the address on each reboot so you have to set them every time

chkserial.py - Small Python program to read the USB serial data and print to screen. I used this code on a Raspberry Pi read the distances from the arduino running the vl53l0x code plugged into the Pi's USB port and drive a robot based on the distance readings.

https://www.adafruit.com/product/3317

http://www.hackrc.net/arduino_lidar_front.JPEG
