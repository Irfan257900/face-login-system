import cv2
import face_recognition
import pickle
import os

ENCODING_FILE = "encodings.pickle"

def login_user():
    if not os.path.exists(ENCODING_FILE):
        print("❌ No registered faces.")
        return "No data"

    with open(ENCODING_FILE, "rb") as f:
        data = pickle.load(f)

    cam = cv2.VideoCapture(0)
    print("[INFO] Scanning...")

    while True:
        ret, frame = cam.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            matches = face_recognition.compare_faces(data["encodings"], encoding)
            name = "Unknown"

            if True in matches:
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}
                for i in matchedIdxs:
                    counts[data["names"][i]] = counts.get(data["names"][i], 0) + 1
                name = max(counts, key=counts.get)
                print(f"✅ Welcome, {name}!")
                cam.release()
                cv2.destroyAllWindows()
                return name

        cv2.imshow("Face Login - Press 'q' to cancel", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    return "Login Failed"
