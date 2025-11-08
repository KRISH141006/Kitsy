# 🧠 Kitsy – A Simple Desktop Assistant

## 📝 Project Definition
**Shutdown, Restart and Logout Computer with Python**

---

## 📘 Description
Kitsy is a simple **voice-controlled desktop assistant** created using **Python**.  
It can **shut down**, **restart**, or **log out** of your computer through **voice commands**.  
The project demonstrates how speech recognition and system commands can be combined to automate basic computer operations.

---

## 🚀 Introduction
Kitsy is **version 1** of a personal desktop assistant designed for Windows systems.  
It uses Python libraries to recognize speech, process it, and respond with spoken feedback.  
Currently, Kitsy performs **system operations** such as:
- Shutting down the computer  
- Restarting the computer  
- Logging off the current user  
- (Optional) Putting the computer to sleep  

---

## ⚙️ How It Works

### 1. Speech Input
- The program listens to the microphone using the `speech_recognition` module.  
- It uses **Google Speech-to-Text API** to convert the user’s voice into text.

### 2. Command Detection
- After converting speech to text, Kitsy checks for specific keywords such as:
  - `"shutdown"` → Shuts down the PC  
  - `"restart"` → Restarts the PC  
  - `"log out"` → Logs off the user  
  - `"sleep"` → Puts the system to sleep  
- These commands are executed using `os.system()` calls.

### 3. Voice Output
- Kitsy responds verbally using the `pyttsx3` text-to-speech engine.  
- It uses the **Microsoft Heera** (Indian English) voice, which is configured offline via the `heeraConfig.py` module.  
- Example feedback:  
  - “Okay, shutting down the computer.”  
  - “Restarting now.”  

---

## 🧩 Libraries Used
| Library | Purpose |
|----------|----------|
| `speech_recognition` | Converts speech to text using Google API |
| `pyttsx3` | Converts text to speech (offline TTS) |
| `os` | Executes system-level commands |
| `time` | Handles delays before executing operations |
| `pyaudio` | Captures audio from the microphone |

---

## 💻 Installation & Setup

### 🐍 Python Version
This project is developed and tested on **Python 3.10.11**.  
It is recommended to use this or a compatible version for best results.
