import requests
import json
import pandas as pd

## dictionary of students and their addresses
def prepare_data():
    
    ## columns = ["name", A-number, "address", points]
    students = pd.read_csv("students.csv")

    addresses = students[['a_number', 'address']].set_index('a_number')
    addresses.to_json("students.json")
    grades = students[['a_number', 'points']].set_index('a_number')
    grades.to_json("grades.json")


    return addresses.to_dict(), grades.to_dict()

# Replace with your Canvas instance URL and API token
BASE_URL = "https://yourcanvasinstance.instructure.com/api/v1"
ACCESS_TOKEN = "your_access_token"
COURSE_ID = 1234  # Replace with your course ID
ASSIGNMENT_ID = 5678  # Replace with your assignment ID

def update_grade(user_id, grade):
    url = f"{BASE_URL}/courses/{COURSE_ID}/assignments/{ASSIGNMENT_ID}/submissions/{user_id}"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "submission": {
            "posted_grade": grade
        }
    }
    response = requests.put(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Successfully updated grade for user {user_id}")
    else:
        print(f"Failed to update grade: {response.status_code}, {response.text}")


## TODO: view the emitted events and update grades

def update_grades(students, grades):
    
    events = pd.read_csv("tokens_burned_events.csv")

    for value in students.values():
        if value in events['Sender'].values:
            ## get the index of the value
            index = events[events['Sender'] == value].index[0]
            grade = events['Amount Burned'][index]
            user_id = value
            update_grade(user_id, grade)
        else:
            print(f"User {value} did not burn any tokens")


