# 🧙‍♀️ Invisibility Cloak using Python & OpenCV

✨ Ever wished you could disappear like Harry Potter under his invisibility cloak?  
With this Python + OpenCV project, you can! It detects a specific color (like red) and replaces it with the background in real time — creating an invisibility illusion using your webcam.

---

## 🎥 Demo
![Demo Screenshot or GIF](demo.gif)

---

## 🚀 How It Works

1. Captures the background frame
2. Detects the cloak color using HSV masking (e.g., red)
3. Masks the cloak and replaces it with the saved background
4. Real-time display makes the person appear invisible!

---

## 🛠️ Tech Stack

- Python 🐍
- OpenCV 🎥
- NumPy ➕
- (Optional) `playsound` for magical sound effects ✨

---

## 📦 Installation & Run Instructions

### 🔧 Setup

```bash
git clone https://github.com/sandhya-tomar/InvisibilityCloak.git
cd InvisibilityCloak
pip install -r requirements.txt

🎮 Run the App
python app.py

🧥 Wear a red cloak (or any target color set in code)
🎥 Stand in front of your webcam
🪄 Watch yourself disappear!

Press q to quit.

📚 References & Credits
Inspired by Harry Potter’s iconic invisibility cloak 🧙‍♂️
Based on tutorials by CodeWithHarry, Murtaza's Workshop, and OpenCV docs
