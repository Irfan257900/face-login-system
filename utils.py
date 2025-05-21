import os
import cv2
import face_recognition
import pickle

DATASET_DIR = "dataset"
ENCODING_FILE = "encodings.pickle"

def capture_face(name):
    cam = cv2.VideoCapture(0)
    count = 0
    user_dir = os.path.join(DATASET_DIR, name)
    os.makedirs(user_dir, exist_ok=True)

    while count < 5:
        ret, frame = cam.read()
        if not ret:
            break
        cv2.imshow("Register - Press 's' to save face", frame)
        k = cv2.waitKey(1)
        if k % 256 == ord('s'):
            img_path = f"{user_dir}/{count}.jpg"
            cv2.imwrite(img_path, frame)
            count += 1
            print(f"[INFO] Saved {img_path}")
        elif k % 256 == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

def encode_faces():
    known_encodings = []
    known_names = []

    for name in os.listdir(DATASET_DIR):
        user_dir = os.path.join(DATASET_DIR, name)
        for img_name in os.listdir(user_dir):
            img_path = os.path.join(user_dir, img_name)
            image = cv2.imread(img_path)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(rgb)
            encodings = face_recognition.face_encodings(rgb, boxes)
            for encoding in encodings:
                known_encodings.append(encoding)
                known_names.append(name)

    data = {"encodings": known_encodings, "names": known_names}
    with open(ENCODING_FILE, "wb") as f:
        pickle.dump(data, f)

    print("[INFO] Encodings saved.")
