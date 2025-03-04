import RPi.GPIO as GPIO
from time import sleep

# GPIO setup
GPIO.setmode(GPIO.BCM)

redPin = 12
greenPin = 19
bluePin = 13
PB1_PIN = 5
PB2_PIN = 6

GPIO.setup([redPin, greenPin, bluePin], GPIO.OUT)
GPIO.setup([PB1_PIN, PB2_PIN], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# PWM setup
freq = 100
red_pwm = GPIO.PWM(redPin, freq)
green_pwm = GPIO.PWM(greenPin, freq)
blue_pwm = GPIO.PWM(bluePin, freq)

red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

state = 0

def turnOff():
    red_pwm.ChangeDutyCycle(0)
    green_pwm.ChangeDutyCycle(0)
    blue_pwm.ChangeDutyCycle(0)

# Main loop
while True:
    pb1_state = GPIO.input(PB1_PIN)
    pb2_state = GPIO.input(PB2_PIN)
    print(f"PB1: {pb1_state}, PB2: {pb2_state}, State: {state}")

    if pb1_state:
        state = (state + 1) % 5
        sleep(0.3)
    if pb2_state:
        state = 0
        turnOff()
        sleep(0.3)
    
    if state == 1:
        red_pwm.ChangeDutyCycle(100)
        green_pwm.ChangeDutyCycle(0)
        blue_pwm.ChangeDutyCycle(0)
    elif state == 2:
        red_pwm.ChangeDutyCycle(0)
        green_pwm.ChangeDutyCycle(0)
        blue_pwm.ChangeDutyCycle(75)
    elif state == 3:
        red_pwm.ChangeDutyCycle(100)
        green_pwm.ChangeDutyCycle(100)
        blue_pwm.ChangeDutyCycle(0)
    elif state == 4:
        red_pwm.ChangeDutyCycle(0)
        green_pwm.ChangeDutyCycle(25)
        blue_pwm.ChangeDutyCycle(0)
    else:
        turnOff()
        sleep(0.3)

# Cleanup after exiting the loop (manually terminate the script to reach here)
red_pwm.stop()