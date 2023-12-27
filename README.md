Mouse Movement and Webcam Capture App

This Flask application captures real-time mouse movement coordinates and allows users to take screenshots by pressing the left mouse button. The captured images are streamed to a web interface, providing a live video feed from the connected webcam. Additionally, the mouse coordinates are stored in an SQLite database for future reference.

Features:

Real-time mouse movement tracking
Webcam video feed with live streaming
Capture screenshots by pressing the left mouse button
Coordinates of the mouse cursor saved to an SQLite database
Requirements:

Flask
OpenCV3
NumPy
How to Use:

Run the application.
Access the video feed at /video_feed.
Capture screenshots by visiting /take_screenshot and pressing the left mouse button.
Note: Ensure that necessary permissions are granted for webcam access.

Installation:

bash
Copy code
pip install flask opencv-python numpy
Database Setup:

SQLite database: coordinates.db
Table: coordinates (id, x, y)
Author:
Mladen Angelov

Feel free to explore the code and contribute!
