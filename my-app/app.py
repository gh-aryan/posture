import cv2
from flask import Flask, render_template, Response, url_for
from posture import sitting_posture_estimation

app = Flask(__name__)

running  = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    global running
    
    if not running :
        running  = True

    def generate():
        global running
        for response in sitting_posture_estimation():
            if not running:
                break
            yield response

    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop')
def stop():
    global running
    running = False
    return 'script stopped'

@app.route('/start')
def start():
    global running
    running = True
    return 'script started'


if __name__ == '__main__':
    app.run(debug=True)
