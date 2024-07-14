import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
import os
import glob
import numpy as np
import cv2
from gpiozero import Servo

# Define GPIO pins for Ultrasonic Sensor
TRIG = 23
ECHO = 24

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Initialize ADC for other sensors
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)

# Initialize Servo motor for camera control
servo = Servo(12)

# Function to measure distance using Ultrasonic Sensor
def measure_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

# Function to read analog sensors (example for one sensor)
def read_analog_sensor():
    return chan.value, chan.voltage

# Function to capture image from Pi Camera
def capture_image():
    # Use picamera or OpenCV to capture image
    # Example using OpenCV:
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return frame

# Main loop for data collection
while True:
    # Read sensor data
    ultrasonic_distance = measure_distance()
    adc_value, adc_voltage = read_analog_sensor()
    
    # Capture image from Pi Camera
    frame = capture_image()
    
    # Process data (send to AWS, perform AI processing, etc.)
    # Example: Send data to AWS IoT Core using MQTT
    
    # Sleep for some time before next iteration
    time.sleep(1)
