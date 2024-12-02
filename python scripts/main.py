from canvas_script import *
from mint_coins import *
from read_events import *
import os



# create CLI UI for the user to interact with the script

def main():
    grades = prepare_data()
    while True:
        print("\n1. Mint Coins")
        print("2. Update Grades")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            mint_coins("grades.json")
        elif choice == "2":
            read_events()
            update_grades(grades)

        elif choice == "3":
            print("Exiting...")
            os.remove("grades.json")
            os.remove("tokens_burned_events.csv")

            break

    
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
