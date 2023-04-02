import RPi.GPIO as GPIO
import time

låg_status = "lukket"

def getHCSRdata():

    # Set GPIO pin numbers for the HC-SR04 ultrasonic sensor
    GPIO_TRIGGER = 23
    GPIO_ECHO = 24
    
    # Set GPIO mode and setup pins
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    
    # Send a 10 microsecond pulse to the sensor to trigger a measurement
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    
    # Measure the duration of the echo signal
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()  
    TimeElapsed = StopTime - StartTime
    
    # Convert the duration to distance in cm using the speed of sound
    distance = round((TimeElapsed * 34300) / 2, 1)
    
    # Calculate the percentage of the tank that is filled
    # percentage = round(-1.0204 * distance + 102.04)
    percentage = round((50 - distance) / 0.5)
    
    # Ensure that the percentage value is within 0-100 range
    if percentage < 0:
        percentage = 0
    elif percentage > 100:
        percentage = 100
    
    # Return the percentage value if the tank is closed, otherwise return None
    # if låg_status == "lukket":
    #     return percentage
    # else:
    #     return None

    return percentage


# percentage = getHCSRdata()
