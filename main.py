from canvas_script import *
from mint_coins import *
from read_events import *
import os


# create CLI UI for the user to interact with the script

def main():
    students, grades = prepare_data()
    while True:
        print("\n1. Mint Coins")
        print("2. Read Events")
        print("3. Update Grades")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            mint_coins()
        elif choice == "2":
            read_events()
        elif choice == "3":
            grading()
        elif choice == "4":
            print("Exiting...")
            os.remove("students.json")
            os.remove("grades.json")
            break
        else:
            print("Invalid choice. Please try again.")