from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit
from camera import Camera


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
socketio = SocketIO(app)


# do something here!!!!!!!!!!!!!!!!
def processImage(input):
    """where the magic happens!"""
    return input


@socketio.on('input image', namespace='/test')
def test_message(input):
    print "got input image: {}".format(input)
    result = processImage(input)
    emit('new image', result)


@socketio.on('connect', namespace='/test')
def test_connect():
    print "client connected"


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""

    print "starting to generate frames!"
    while True:
        frame = camera.get_frame()
        print "generating frames..."
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    socketio.run(app)
