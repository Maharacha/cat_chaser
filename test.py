from src.motors_pwm import *
from src.distance import *
from src.avoidance import *

def distance_test():
    distance_init()
    try:
        while True:
            dist = get_distance()
            if dist < 20:
                print("%.2f" % dist)
    # If you press CTRL+C, cleanup and stop
    except KeyboardInterrupt:
        # Reset GPIO settings
        GPIO.cleanup()

        return

def avoidance_test():
    all_motors_init()
    distance_init()
    try:
        while True:
            a_forwards(25)
            b_forwards(25)
            time.sleep(0.1)
            if is_near_obstacle():
                all_motors_off()
                avoid_obstacle()
                
    # If you press CTRL+C, cleanup and stop
    except KeyboardInterrupt:
        all_motors_off()
        # Reset GPIO settings
        GPIO.cleanup()

        return

def main():
    return

if __name__ == '__main__':
    distance_test()
