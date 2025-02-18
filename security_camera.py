import cv2
import time
import datetime

cap = cv2.VideoCapture(0)  # Capture video from the first available video source

# Load pre-trained Haar cascades for face and body detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")  # Classifier for detecting faces
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")  # Classifier for detecting bodies

detection = False  # Boolean to check if motion is detected
detection_stopped_time = None  # Keeps track of when motion stopped
timer_started = False  # Boolean to start the recording stop timer
SECONDS_TO_RECORD_AFTER_DETECTION = 5  # How long to keep recording after no detection

frame_size = (int(cap.get(3)), int(cap.get(4)))  # Get frame width and height
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Define codec for saving video

while True:
    _, frame = cap.read()  # Read one frame from the video capture device
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale for analysis

    """
    detectMultiScale returns a list of positions (x, y, width, height) of all detected objects.
    - The second parameter is the scale factor: between 1.1 and 1.5 (lower = more accurate but slower)
    - The third parameter is minNeighbors: controls false positives (higher value = stricter detection)
    """
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = body_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) + len(bodies) > 0:  # If at least one face or body is detected
        if detection:
            timer_started = False  # Reset stop timer if already recording
        else:
            detection = True  # Set detection to True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")  # Create timestamp for filename
            out = cv2.VideoWriter(
                f"{current_time}.mp4", fourcc, 20, frame_size)  # Start video writer
            print("Started Recording!\nPress 'q' to quit")
    elif detection:  # If no more motion detected
        if timer_started:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()  # Stop recording
                print('Stop Recording!')
        else:
            timer_started = True  # Start timer to stop recording
            detection_stopped_time = time.time()

    if detection:
        out.write(frame)  # Write frame to video file

    # Draw blue rectangles around detected faces
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)  # Blue rectangle (BGR format)

    # Draw blue rectangles around detected bodies
    for (x, y, width, height) in bodies:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)  # Blue rectangle (BGR format)

    cv2.imshow("Camera", frame)  # Show the frame with detections

    if cv2.waitKey(1) == ord('q'):  # Press 'q' to exit the loop
        break

out.release()  # Release video writer
cap.release()  # Release camera resource
cv2.destroyAllWindows()  # Close the OpenCV window
