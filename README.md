# PyQt5 Stopwatch ⏱️

A simple desktop stopwatch application built using **Python** and **PyQt5**.  
The app features start, stop, and reset functionality with a clean and responsive GUI.

---

## ✨ Features

- Start, stop, and reset controls  
- Time tracking with hours, minutes, seconds, and milliseconds  
- Smooth updates using `QTimer`  
- Clean and minimal PyQt5 user interface  

---

## 🛠️ Technologies Used

- Python 3
- PyQt5

---

## 🚀 How It Works

- `QTime` is used to store and update the elapsed time
- `QTimer` triggers updates every 10 milliseconds
- Button clicks control the stopwatch state using Qt signals and slots
