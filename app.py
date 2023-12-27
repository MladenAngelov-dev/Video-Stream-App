from flask import Flask, render_template, Response, request, g
import cv2
import numpy as np
import sqlite3
import asyncio

app = Flask(__name__)

camera = cv2.VideoCapture(0)  # use 0 for web camera

# SQLite database setup
DATABASE = 'coordinates.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS coordinates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                x INTEGER,
                y INTEGER
            )
        ''')
        db.commit()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/take_screenshot')
def take_screenshot():
    # Capture a single frame
    success, frame = camera.read()
    if success:
        # Save the frame as an image file
        cv2.imwrite('screenshot.jpg', frame)

        # Get the mouse coordinates from the request
        x = int(request.args.get('x', 0))
        y = int(request.args.get('y', 0))

        # Save the coordinates to the SQLite database
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO coordinates (x, y) VALUES (?, ?)', (x, y))
        db.commit()

    return "Screenshot taken!"


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
