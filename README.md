# 📸 SnapClass – AI Powered Smart Attendance System

SnapClass is an AI-powered Smart Attendance System that automates classroom attendance using **Face Recognition**, **Voice Biometrics**, and **QR Code-based Student Enrollment**. The application is built with **Python** and provides an easy-to-use interface for teachers to manage attendance efficiently.

---

# 🚀 Features

- 📸 Face Recognition Attendance
- 🎙️ Voice Authentication Attendance
- 📱 QR Code Student Enrollment
- 👨‍🏫 Teacher Dashboard
- 👨‍🎓 Student Management
- 📂 Subject Management
- 📝 Attendance Reports
- 🤖 Automatic Student Enrollment
- 📷 Capture Images from Camera
- 💾 Database Integration
- ⚡ Fast and Lightweight Desktop Application

---

# 🖥️ Tech Stack

- Python
- CustomTkinter / Tkinter
- OpenCV
- Face Recognition
- Speech Recognition
- SQLite
- NumPy
- Pillow
- QR Code
- PyAudio
- Librosa

---

# 📂 Project Structure

```
SnapClass/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── components/
│   │   ├── dialog_add_photo.py
│   │   ├── dialog_auto_enroll.py
│   │   ├── dialog_create_subject.py
│   │   ├── dialog_enroll.py
│   │   ├── dialog_share_subject.py
│   │   ├── dialog_voice_attendance.py
│   │   ├── dialog_attendance_results.py
│   │   ├── header.py
│   │   ├── footer.py
│   │   └── subject_card.py
│   │
│   ├── database/
│   │   ├── config.py
│   │   └── db.py
│   │
│   ├── pipelines/
│   │   ├── face_pipeline.py
│   │   └── voice_pipeline.py
│   │
│   ├── screens/
│   │   ├── home_screen.py
│   │   ├── teacher_screen.py
│   │   └── student_screen.py
│   │
│   └── ui/
│       └── base_layout.py
│
└── assets/
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/SnapClass.git
cd SnapClass
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

---

# 📸 Attendance Workflow

### Step 1

Create a Subject.

### Step 2

Enroll Students.

### Step 3

Register Student Face.

### Step 4

Register Student Voice.

### Step 5

Generate QR Code for Class.

### Step 6

Take Attendance using:

- Face Recognition
- Voice Recognition
- QR Verification

### Step 7

View Attendance Report.

---

# 🧠 AI Pipelines

## 📸 Face Recognition Pipeline

- Capture classroom image/video
- Detect faces
- Extract facial embeddings
- Match against enrolled students
- Mark attendance automatically

---

## 🎙️ Voice Recognition Pipeline

- Record student's voice
- Extract voice features
- Compare with enrolled voice samples
- Verify identity
- Mark attendance

---

## 📱 QR Enrollment

- Generate QR for subjects
- Students scan QR
- Automatic enrollment into classroom

---

# 📊 Core Modules

- Teacher Management
- Student Management
- Subject Management
- Face Enrollment
- Voice Enrollment
- QR Enrollment
- Attendance Processing
- Attendance Report Generation

---

# 🔥 Future Enhancements

- Cloud Database
- Mobile Application
- Live Classroom Attendance
- Multi-Class Support
- Email Notifications
- Analytics Dashboard
- AI Attendance Statistics
- Face Anti-Spoofing
- Liveness Detection
- Dark Mode

---

# 📦 Requirements

Example dependencies:

```
opencv-python
numpy
Pillow
customtkinter
face_recognition
librosa
SpeechRecognition
PyAudio
qrcode
sqlite3
```

Install all requirements:

```bash
pip install -r requirements.txt
```

---

# 📈 Project Workflow

```
Teacher
    │
    ▼
Create Subject
    │
    ▼
Enroll Students
    │
    ▼
Face & Voice Registration
    │
    ▼
Start Attendance
    │
    ├─────────────► Face Recognition
    │
    ├─────────────► Voice Recognition
    │
    └─────────────► QR Verification
    │
    ▼
Attendance Stored
    │
    ▼
Attendance Reports
```

---

# 👨‍💻 Author

**Lalesh Pawar**

Computer Science Engineer | AI & Data Science Enthusiast

---

# 📄 License

This project is developed for educational and research purposes.

```
MIT License
```

---

# ⭐ Support

If you like this project, don't forget to ⭐ the repository on GitHub!
