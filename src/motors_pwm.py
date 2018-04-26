import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

# Set variables for the GPIO motor pins
pinMotorAForwards = 10  #  left motor
pinMotorABackwards = 9  #  left motor
pinMotorBForwards = 7  #  right motor
pinMotorBBackwards = 8  #  right motor

# pwmMotorAForwards = 0
# pwmMotorABackwards = 0
# pwmMotorBForwards = 0
# pwmMotorBBackwards = 0
    
# How many times to turn the pin on and off each second
Frequency = 20

def all_motors_init():
    # Set the GPIO modes
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(pinMotorAForwards, GPIO.OUT)
    GPIO.setup(pinMotorABackwards, GPIO.OUT)
    GPIO.setup(pinMotorBForwards, GPIO.OUT)
    GPIO.setup(pinMotorBBackwards, GPIO.OUT)

    # Set the GPIO to software PWM at 'Frequency' Hertz
    global pwmMotorAForwards
    pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
    global pwmMotorABackwards
    pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
    global pwmMotorBForwards
    pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
    global pwmMotorBBackwards
    pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

    # Start the software PWM with a duty cycle of 0 (i.e. not moving)
    pwmMotorAForwards.start(0)
    pwmMotorABackwards.start(0)
    pwmMotorBForwards.start(0)
    pwmMotorBBackwards.start(0)

def all_motors_off():
    # Turn all motors off
    pwmMotorAForwards.ChangeDutyCycle(0)
    pwmMotorABackwards.ChangeDutyCycle(0)
    pwmMotorBForwards.ChangeDutyCycle(0)
    pwmMotorBBackwards.ChangeDutyCycle(0)

def a_forwards(duty_cycle=25):
    # Turn the left motor forwards
    pwmMotorAForwards.ChangeDutyCycle(duty_cycle)
    pwmMotorABackwards.ChangeDutyCycle(0)

def b_forwards(duty_cycle=25):
    # Turn the right motor forwards
    pwmMotorBForwards.ChangeDutyCycle(duty_cycle)
    pwmMotorBBackwards.ChangeDutyCycle(0)

def a_backwards(duty_cycle=25):
    # Turn the left motor backwards
    pwmMotorAForwards.ChangeDutyCycle(0)
    pwmMotorABackwards.ChangeDutyCycle(duty_cycle)

def b_backwards(duty_cycle=25):
    # Turn the right motor backwards
    pwmMotorBForwards.ChangeDutyCycle(0)
    pwmMotorBBackwards.ChangeDutyCycle(duty_cycle)

def a_off():
    # Turn the left motor off
    pwmMotorAForwards.ChangeDutyCycle(0)
    pwmMotorABackwards.ChangeDutyCycle(0)

def b_off():
    # Turn the right motor off
    pwmMotorBForwards.ChangeDutyCycle(0)
    pwmMotorBBackwards.ChangeDutyCycle(0)

def all_motors_reset():
    # Reset the GPIO pins (turns off motors too)
    GPIO.cleanup()
