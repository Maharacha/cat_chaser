import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

# Set variables for the GPIO motor pins
pinMotorAForwards = 10  #  left motor
pinMotorABackwards = 9  #  left motor
pinMotorBForwards = 7  #  right motor
pinMotorBBackwards = 8  #  right motor

def all_motors_init():
    # Set the GPIO modes
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(pinMotorAForwards, GPIO.OUT)
    GPIO.setup(pinMotorABackwards, GPIO.OUT)
    GPIO.setup(pinMotorBForwards, GPIO.OUT)
    GPIO.setup(pinMotorBBackwards, GPIO.OUT)

def all_motors_off():
    # Turn all motors off
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)

def a_forward():
    # Turn the left motor forwards
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorAForwards, 1)

def b_forward():
    # Turn the right motor forwards
    GPIO.output(pinMotorBBackwards, 0)
    GPIO.output(pinMotorBForwards, 1)

def a_backwards():
    # Turn the left motor backwards
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorAForwards, 0)

def b_backwards():
    # Turn the right motor backwards
    GPIO.output(pinMotorBBackwards, 1)
    GPIO.output(pinMotorBForwards, 0)

def a_off():
    # Turn the left motor off
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorAForwards, 0)

def b_off():
    # Turn the right motor off
    GPIO.output(pinMotorBBackwards, 0)
    GPIO.output(pinMotorBForwards, 0)

def all_motors_reset():
    # Reset the GPIO pins (turns off motors too)
    GPIO.cleanup()
