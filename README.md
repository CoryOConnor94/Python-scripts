
# Miles to KM Converter

This is a simple **Tkinter-based GUI application** that converts user-inputted miles to kilometers.

## 📌 Features
- **User Input**: Enter miles in the input box.
- **Conversion Calculation**: Converts miles to kilometers using `1 mile = 1.609 km`.
- **Real-Time Update**: Displays the result instantly upon clicking the "Calculate" button.
- **Minimal UI**: A simple, easy-to-use interface.

## 🛠 Prerequisites
- Python 3.x
- Tkinter (included in Python standard library)

## 🚀 Installation & Usage
1. Clone this repository or copy the script.
2. Run the script:
   ```sh
   python miles_to_km.py
   ```
3. Enter a value in miles and click "Calculate" to see the result.

## ⚙️ How It Works
- The user enters a value (in miles).
- The program converts it to kilometers using `km = miles * 1.609`.
- The result is displayed in the UI.

## 📌 Example
```
Input: 5 miles
Output: 8 km
```





# Pomodoro Timer

A **Tkinter-based** Pomodoro timer application that follows the **25-minute work / 5-minute break** technique to enhance productivity.

## 📌 Features
- **Work Timer (25 min)**: Focus session.
- **Short Break (5 min)**: After each work session.
- **Long Break (20 min)**: After every four work sessions.
- **Countdown Timer**: Displays remaining time.
- **Checkmarks for Progress**: Tracks completed Pomodoro cycles.

## 🛠 Prerequisites
- Python 3.x
- Tkinter (included in Python standard library)

## 🚀 Installation & Usage
1. Clone this repository or copy the script.
2. Run the script:
   ```sh
   python pomodoro_timer.py

3. Click **Start** to begin.
4. Click **Reset** to reset the timer.

## ⚙️ How It Works
- Click **Start** → Timer starts at 25:00.
- After each session, it switches to a **5-minute break**.
- Every 4th session → **20-minute break**.
- Checkmarks (`✔`) appear after each work session.

## 📌 Example Output

[Timer Starts] → Work: 25:00
[Short Break] → 5:00
[Timer Resumes] → Work: 25:00
...
✔✔ (2 work sessions completed)


## 📜 License
This project is licensed under the MIT License.
