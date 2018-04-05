from motors_pwm import *
from distance import *

global speed
speed = 30
global near_threshold
near_threshold= 15

# Return True if the ultrasonic sensor sees an obstacle
def is_near_obstacle():
    distance = get_distance()

    # print("IsNearObstacle: "+str(Distance))
    if distance < near_threshold:
        return True
    else:
        return False

# Move back a little, then turn right
def avoid_obstacle():
    # Back off a little
    print("Backwards")
    a_backwards(speed)
    b_backwards(speed)
    time.sleep(0.5)
    all_motors_off()

    # Turn right
    print("Right")
    a_forwards(speed)
    time.sleep(0.75)
    all_motors_off()
