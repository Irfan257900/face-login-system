from utils import capture_face, encode_faces

def register_user(name):
    print(f"[INFO] Registering {name}")
    capture_face(name)
    encode_faces()
