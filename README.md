# Face Login System

A simple face recognition login system with a Tkinter GUI, using OpenCV and the `face_recognition` library.

## Features

- **Register:** Capture a user's face and associate it with their name.
- **Login:** Recognize a user's face and log them in if matched.
- **GUI:** Easy-to-use interface built with Tkinter.

## Requirements

- Python 3.10
- OpenCV (`opencv-python`)
- face_recognition
- dlib
- Pillow
- Tkinter (usually included with Python, but may require `brew install python-tk@3.10` on macOS)

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Irfan257900/face-login-system.git
    cd face-login-system
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3.10 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install opencv-python face_recognition pillow
    ```

4. **(macOS only) If you get Tkinter errors:**
    ```bash
    brew install python-tk@3.10
    ```

## Usage

Run the application:

```bash
python app.py
```

- Click **Register** to add a new user (you'll be prompted for a name and your face will be captured).
- Click **Login** to log in using face recognition.

## File Structure

- `app.py` - Main GUI application
- `register.py` - Handles user registration
- `login.py` - Handles user login
- `utils.py` - Utility functions for face capture and encoding

## Notes

- Face data is stored locally (check the code for details).
- Do **not** commit your virtual environment or large data files to git.
- Use `.gitignore` to exclude `venv/`, `__pycache__/`, etc.

## License

MIT License

---

**Developed by Mohammad Irfan**
