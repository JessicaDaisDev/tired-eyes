# Tired Eyes 👀

**A customizable, terminal-based screen-break reminder built in Python.**


## Video Demonstration

[Watch My Tired Eyes Project Presentation (10 minutes)](https://youtu.be/SUfNT46Fnfc)

This video explains the purpose of Tired Eyes, walks through the Python code, and demonstrates the application. It highlights functions, list management, input validation, error handling, and timer automation.

I developed Tired Eyes independently as my final project for an introductory Python programming course in 2026. I also created a video presentation to explain the problem, the program structure, and a live demonstration.

## Why I built it

It's easy to lose track of time when studying, programming, or working at a computer. Tired Eyes encourages regular breaks through timed, visible reminders and simple eye-rest, stretching, and breathing suggestions.

## Features

- Choose a custom time interval between reminders.
- View the built-in list of break exercises.
- Add your own reminders or remove existing ones.
- Receive a randomly selected activity when the timer expires.
- See a 20-second countdown in the terminal before the cycle repeats.
- Handle invalid menu choices, invalid timer input, and invalid deletion requests.

> **Note:** Tired Eyes runs in a terminal. It clears and redraws the terminal display; it does **not** lock the Windows desktop or prevent switching to other apps. Keep the terminal window open while using it.

## Technologies and concepts

- **Python 3**, using only standard-library modules: `os`, `time`, and `random`
- User-defined functions, loops, conditional statements, lists, `.append()`, and `.pop()`
- Input validation and exception handling (`try`/`except ValueError`)
- Cross-platform terminal clearing using `os.name`

## Run it on Windows

1. Install Python 3 from [python.org](https://www.python.org/downloads/) if it isn't already installed.
2. Download `tired_eyes.py` from this repository.
3. Open **PowerShell** in the folder containing the file.
4. Run:

   ```powershell
   py tired_eyes.py
   ```

   If `py` isn't available, try `python tired_eyes.py`.
5. Select a menu option (`1`–`4`), then set the number of minutes between breaks. For a quick test, enter `0.1` (six seconds).
6. Keep the terminal open. Press **Ctrl+C** to stop the reminder loop.

## Example interaction

```text
--- Setup Menu ---
1. View current break exercises
2. Add a custom break exercise
3. Delete a break exercise
4. Start the Break Enforcer
Select an option (1-4): 4

--- Timer Configuration ---
How many minutes between breaks? (e.g., 20 or 0.1 for testing): 0.1
```

## What I learned

Building this project helped me practice breaking a program into smaller functions, managing a changing list of data, validating user input, handling errors, and explaining code through a recorded presentation.

## Potential future improvements

These are **ideas**, not features in the current version:

- Save customized exercises between sessions.
- Add optional desktop notifications.
- Write automated tests for menu and validation behavior.
- Build a simple graphical or web interface.

## Project context

**Individual Python course project** | **July 2026** | **Jessica Dais**
