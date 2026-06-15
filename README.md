# 🚀 My AI Jarvis — Advanced Desktop Virtual Assistant

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![AI Engine](https://img.shields.io/badge/AI%20Engine-Google%20Gemini-orange.svg)](https://ai.google.dev/)
[![UI Framework](https://img.shields.io/badge/UI-Eel%20%28HTML%2FCSS%2FJS%29-green.svg)](https://github.com/python-eel/Eel)
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)

An elite, full-stack desktop virtual assistant designed to mimic a futuristic AI interface. Jarvis integrates a sleek **web-based GUI** with a powerful backend powered by **Google Gemini AI Core**, enabling intelligent conversation, system automation, and real-time communication tracking.

---

## 🌟 Key Features & Architecture

### 🧠 1. Cognitive Brain (Gemini AI Core)
* Fully integrated with Google's advanced `gemini-pro` generative model.
* Clean, context-aware prompt engineering optimized for voice synthesis.
* Auto-fallback mechanism: If the API or internet is offline, it seamlessly redirects queries to local systems/web scraping to ensure zero downtime.

### 🎨 2. Next-Gen Frontend UI
* Driven by the **Python Eel** library to bridge local scripts with modern web tech.
* Lightweight, responsive dashboard built using HTML5, CSS3 transitions, and vanilla JavaScript.
* Synchronized visual states matching ambient microphone activity.

### 📞 3. Automation & Communication Hub
* **Smart DB Search:** Connects to a local SQLite database (`jarvis.db`) to fetch matching contact logs instantly.
* **WhatsApp Controller:** Handles zero-click automation for sending instant texts or initiating desktop application calls.
* **Media Sync:** Intelligent string parsing for seamless hands-free YouTube playback.

---

## 📊 System Module Map

| Module | Core Responsibility | Key Technologies |
| :--- | :--- | :--- |
| **`main.py`** | Application Entrypoint & Frontend Init | `eel`, `multiprocessing` |
| **`engine/command.py`** | Speech Recognition & Command Router | `speech_recognition`, `regex` |
| **`engine/features.py`**| AI Brain, WhatsApp, YouTube & Database Hub | `google-generativeai`, `pyttsx3`, `sqlite3` |
| **`www/`** | Visual UI Web Interface Layout | `HTML5`, `CSS3`, `JavaScript` |

---

## ⚙️ Installation & Developer Setup

Follow these structured steps to replicate or contribute to this deployment environment:

### Prerequisites
Ensure you have Python 3.8 or above installed on your environment, along with Git.

### 1. Repository Replication
```bash
git clone [https://github.com/Bhavesh-harchandani/My-AI-Jarvis.git](https://github.com/Bhavesh-harchandani/My-AI-Jarvis.git)
cd My-AI-Jarvis