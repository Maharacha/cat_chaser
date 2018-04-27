from flask import Flask, render_template, request, redirect, url_for, make_response, Response
from http import HTTPStatus
import socket
from src.motors_pwm import *
from src.camera import *
from src.avoidance import *

motors_obj = MotorsPwm()
motors_obj.all_motors_init()
avoidance_obj = Avoidance(motors_obj)
camera_obj = Camera()

# Get server ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
server_ip = s.getsockname()[0]
s.close()

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html', server_ip=server_ip)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    global camera_obj
    return Response(gen(camera_obj),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/motor/<action>', methods=['POST'])
def reroute(action):

    if action == 'left':
        motors_obj.b_forwards()
        motors_obj.a_backwards()
    elif action == 'forward':
        motors_obj.a_forwards()
        motors_obj.b_forwards()
    elif action == 'right':
        motors_obj.a_forwards()
        motors_obj.b_backwards()
    elif action == 'reverse':
        motors_obj.a_backwards()
        motors_obj.b_backwards()
    elif action == 'stop':
        motors_obj.all_motors_off()
    else:
        print('Wrong command')
    
    # response = make_response(redirect(url_for('index')))
    return('', HTTPStatus.NO_CONTENT)

app.run(debug=False, threaded=True, host='0.0.0.0', port=8000) 
