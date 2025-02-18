# Security Camera with Motion Detection

A Python app that uses OpenCV to detect faces and bodies in real-time. It starts recording when motion is detected and saves the video with a timestamp. Blue rectangles highlight detected faces and bodies.

## Features
- Real-time face and body detection using Haar cascades.
- Starts recording when motion (face/body) is detected.
- Saves video with a timestamped filename.
- Stops recording after a set time once motion stops.
- Blue rectangles around detected faces and bodies.

## Requirements
- Python 3.x
- OpenCV

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/security-camera-app.git

2. Navigate to the project directory:
   ```bash
   cd security-camera-app
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Usage
  Run the app:
   ```bash
   python security_camera.py
  Press 'q' to quit the application.
