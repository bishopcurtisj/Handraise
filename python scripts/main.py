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
        print("3. Read Events")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            mint_coins("grades.json")
        elif choice == "2":
            read_events()
            update_grades(grades)
            print("Grades updated successfully!")
            os.remove("tokens_burned_events.csv")

        elif choice == "3":
            print("Reading events...")
            read_events()
            test_grades(grades)
    
        elif choice == "4":
            print("Exiting...")
            os.remove("grades.json")

            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
