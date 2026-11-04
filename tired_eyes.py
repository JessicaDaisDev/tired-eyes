"""
Name: Jessica Dais
Date: 07/31/26
Description: "Tired Eyes" Screen Break Enforcer. This program helps remote 
workers and students avoid eye strain by enforcing regular breaks. Users can 
customize break intervals, add/delete custom health exercises to a list, and see a 
clear, full-screen console warning when it is time to take a break.
"""

import os
import time
import random

def add_exercise(exercise_list):
    """
    Prompts the user to input a new stretch or breathing instruction
    and appends it to the existing exercise list.
    
    Parameters:
    exercise_list (list): The list containing break exercise strings.
    
    Returns:
    None
    """
    print("\n--- Add a New Exercise ---")
    new_exercise = input("Enter a new stretch, breathing instruction, or reminder: ").strip()
    if new_exercise:
        exercise_list.append(new_exercise)
        print(f"Success: '{new_exercise}' has been added to your list!")
    else:
        print("Error: Exercise description cannot be empty.")

def view_exercises(exercise_list):
    """
    Loops through and prints all current stretch and breathing 
    exercises with numbering so the user can verify them.
    
    Parameters:
    exercise_list (list): The list containing break exercise strings.
    
    Returns:
    None
    """
    print("\n--- Current Break Exercises ---")
    if not exercise_list:
        print("Your exercise list is currently empty.")
    else:
        for index, exercise in enumerate(exercise_list, start=1):
            print(f"{index}. {exercise}")

def delete_exercise(exercise_list):
    """
    Displays current exercises and allows the user to safely remove 
    an exercise from the list by entering its list number.
    
    Parameters:
    exercise_list (list): The list containing break exercise strings.
    
    Returns:
    None
    """
    print("\n--- Delete an Exercise ---")
    if not exercise_list:
        print("There are no exercises available to delete.")
        return
        
    # Show the current list first so they know the numbers
    view_exercises(exercise_list)
    
    try:
        choice = int(input("\nEnter the number of the exercise you want to delete: "))
        # Adjust for 0-based indexing (e.g., item #1 is index 0)
        if 1 <= choice <= len(exercise_list):
            removed = exercise_list.pop(choice - 1)
            print(f"Success: Removed '{removed}' from your list.")
        else:
            print("Error: That number is not on the list.")
    except ValueError:
        print("Error: Please enter a valid whole number.")

def enforce_break(exercise_list, interval_minutes):
    """
    Runs the background timer loop. Pauses execution for the set interval,
    selects a random exercise, clears the console, and displays an unavoidable
    20-second break countdown banner.
    
    Parameters:
    exercise_list (list): The list containing break exercise strings.
    interval_minutes (float): How long to wait between breaks in minutes.
    
    Returns:
    None
    """
    print(f"\n[System] Tired Eyes is active! Running in the background...")
    print(f"[System] A break will be enforced every {interval_minutes} minute(s).")
    print("[System] Keep this window open. Press Ctrl+C here to stop.")
    
    interval_seconds = interval_minutes * 60
    
    try:
        while True:
            # Wait in the background for the designated interval
            time.sleep(interval_seconds)
            
            # Select a random exercise reminder from the list
            if exercise_list:
                break_message = random.choice(exercise_list)
            else:
                break_message = "Look away from your screen and relax your eyes!"
            
            # Detect operating system and clear the terminal screen
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Display a highly visible text-based alert block
            print("\n" + "=" * 60)
            print(" !!! TIME FOR A SCREEN BREAK !!! ".center(60))
            print("=" * 60)
            print(f"\nYOUR REMINDER:\n-> {break_message}\n")
            print("=" * 60)
            
            # Run a live visual countdown timer in the console for 20 seconds
            for seconds_left in range(20, 0, -1):
                print(f"Screen unlocking in {seconds_left} seconds... Please look away!", end="\r")
                time.sleep(1)
            
            # Clear the break screen text and go back to background mode
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n[System] Break finished. Screen unlocked.")
            print(f"[System] Next break in {interval_minutes} minute(s). Timer restarted.")
            print("[System] Press Ctrl+C to close the program.")
            
    except KeyboardInterrupt:
        print("\n\n[System] Tired Eyes stopped. Take care of your eyes!")

def main():
    """
    Main function that manages the program startup, initializes the
    exercise data list, handles settings customization, and starts the script.
    
    Parameters:
    None
    
    Returns:
    None
    """
    # Initialize the starting list with default exercises
    exercises = [
        "Follow the 20-20-20 rule: Look at something 20 feet away for 20 seconds.",
        "Roll your shoulders backwards 5 times, then forwards 5 times.",
        "Close your eyes tightly for 5 seconds, then open them wide.",
        "Stand up, stretch your arms over your head, and take a deep breath.",
        "Stand up and walk around your room or desk for a moment."
    ]
    
    print("========================================")
    print("       WELCOME TO TIRED EYES            ")
    print("========================================")
    
    # Setup interactive menu loop to manage exercises before starting timer
    while True:
        print("\n--- Setup Menu ---")
        print("1. View current break exercises")
        print("2. Add a custom break exercise")
        print("3. Delete a break exercise")
        print("4. Start the Break Enforcer")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            view_exercises(exercises)
        elif choice == '2':
            add_exercise(exercises)
        elif choice == '3':
            delete_exercise(exercises)
        elif choice == '4':
            break  # Exit setup menu and proceed to start the program
        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")
            
    # Gather custom timer settings from user
    print("\n--- Timer Configuration ---")
    while True:
        try:
            minutes = float(input("How many minutes between breaks? (e.g., 20 or 0.1 for testing): "))
            if minutes > 0:
                break
            else:
                print("Please enter a positive number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    # Launch the background enforcer function
    enforce_break(exercises, minutes)

if __name__ == "__main__":
    main()
