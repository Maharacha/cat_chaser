from src.motors_pwm import *
from src.distance import *
import threading
import time

class Avoidance():

    def __init__(self, motors_obj):
        self.motors_obj = motors_obj
        distance_init()
        self.speed = 30
        self.near_threshold = 15
        thread = threading.Thread(target=self._thread)
        thread.start()
    
    # Return True if the ultrasonic sensor sees an obstacle
    def is_near_obstacle(self):
        distance = get_distance()
        
        # print("IsNearObstacle: "+str(Distance))
        if distance < self.near_threshold and distance > 0:
            return True
        else:
            return False

    # Move back a little, then turn right
    def avoid_obstacle(self):
        # Back off a little
        self.motors_obj.a_backwards(self.speed)
        self.motors_obj.b_backwards(self.speed)
        time.sleep(0.5)
        self.motors_obj.all_motors_off()
        '''
        # Turn right
        self.motors_obj.a_forwards(self.speed)
        time.sleep(0.75)
        self.motors_obj.all_motors_off()
        '''
    def _thread(self):
        while True:
            if self.is_near_obstacle():
                self.avoid_obstacle()
