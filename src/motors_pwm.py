import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library
import threading


class MotorsPwm():

    def __init__(self):
        # Set variables for the GPIO motor pins
        self.pinMotorAForwards = 10  #  left motor
        self.pinMotorABackwards = 9  #  left motor
        self.pinMotorBForwards = 7  #  right motor
        self.pinMotorBBackwards = 8  #  right motor
        
        # How many times to turn the pin on and off each second
        self.frequency = 20
    
    def all_motors_init(self):
        # Set the GPIO modes
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        GPIO.setup(self.pinMotorAForwards, GPIO.OUT)
        GPIO.setup(self.pinMotorABackwards, GPIO.OUT)
        GPIO.setup(self.pinMotorBForwards, GPIO.OUT)
        GPIO.setup(self.pinMotorBBackwards, GPIO.OUT)
        
        # Set the GPIO to software PWM at 'Frequency' Hertz
        self.pwmMotorAForwards = GPIO.PWM(self.pinMotorAForwards, self.frequency)
        self.pwmMotorABackwards = GPIO.PWM(self.pinMotorABackwards, self.frequency)
        self.pwmMotorBForwards = GPIO.PWM(self.pinMotorBForwards, self.frequency)
        self.pwmMotorBBackwards = GPIO.PWM(self.pinMotorBBackwards, self.frequency)
        
        # Start the software PWM with a duty cycle of 0 (i.e. not moving)
        self.pwmMotorAForwards.start(0)
        self.pwmMotorABackwards.start(0)
        self.pwmMotorBForwards.start(0)
        self.pwmMotorBBackwards.start(0)
        
    def all_motors_off(self):
        # Turn all motors off
        self.pwmMotorAForwards.ChangeDutyCycle(0)
        self.pwmMotorABackwards.ChangeDutyCycle(0)
        self.pwmMotorBForwards.ChangeDutyCycle(0)
        self.pwmMotorBBackwards.ChangeDutyCycle(0)
        
    def a_forwards(self, duty_cycle=25):
        # Turn the left motor forwards
        self.pwmMotorAForwards.ChangeDutyCycle(duty_cycle)
        self.pwmMotorABackwards.ChangeDutyCycle(0)
        
    def b_forwards(self, duty_cycle=25):
        # Turn the right motor forwards
        self.pwmMotorBForwards.ChangeDutyCycle(duty_cycle)
        self.pwmMotorBBackwards.ChangeDutyCycle(0)
        
    def a_backwards(self, duty_cycle=25):
        # Turn the left motor backwards
        self.pwmMotorAForwards.ChangeDutyCycle(0)
        self.pwmMotorABackwards.ChangeDutyCycle(duty_cycle)

    def b_backwards(self, duty_cycle=25):
        # Turn the right motor backwards
        self.pwmMotorBForwards.ChangeDutyCycle(0)
        self.pwmMotorBBackwards.ChangeDutyCycle(duty_cycle)

    def a_off(self):
        # Turn the left motor off
        self.pwmMotorAForwards.ChangeDutyCycle(0)
        self.pwmMotorABackwards.ChangeDutyCycle(0)

    def b_off(self):
        # Turn the right motor off
        self.pwmMotorBForwards.ChangeDutyCycle(0)
        self.pwmMotorBBackwards.ChangeDutyCycle(0)

    def all_motors_reset(self):
        # Reset the GPIO pins (turns off motors too)
        GPIO.cleanup()

        
