from canvas_script import *
from mint_coins import *
from read_events import *
import os

def test(file_path):
    # Load data from JSON
    with open(file_path, "r") as file:
        data = json.load(file)

    # Prepare recipients and amounts
    recipients = [entry["address"] for entry in data.values()]
    amounts = [entry["points"] for entry in data.values()]

    print("done")

# create CLI UI for the user to interact with the script

def main():
    grades = prepare_data()
    test("grades.json")
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
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
