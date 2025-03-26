import cv2
import face_recognition
import numpy as np
import sqlite3

# Database Connection
conn = sqlite3.connect("face_database.db")
cursor = conn.cursor()

known_faces = []
known_names = []

# Fetch names and image paths from the database
cursor.execute("SELECT name, image_path FROM users")
for row in cursor.fetchall():
    name, image_path = row
    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)[0]
    known_faces.append(encoding)
    known_names.append(name)

# Start Camera
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB

    # Detect Faces
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"
        details = ""

        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]

            # Fetch Details from Database
            cursor.execute("SELECT * FROM users WHERE name=?", (name,))
            user_data = cursor.fetchone()
            details = f"Name: {user_data[1]}, Age: {user_data[2]}, Address: {user_data[3]}"

        # Display Box & Name on Screen
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, details, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Face Recognition System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close all windows
video_capture.release()
cv2.destroyAllWindows()
conn.close()