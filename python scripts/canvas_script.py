import requests
import json
import pandas as pd 
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

## dictionary of students and their addresses
def prepare_data():
    
    ## columns = ["name", A-number, "address", points]
    students = pd.read_csv("students.csv")

    grades = students[['a_number', 'address', 'points']].set_index('a_number').to_dict(orient='index')

    with open('grades.json', 'w') as f:
        json.dump(grades, f, indent=4)
    

    return grades


# Replace with your Canvas instance URL and API token
BASE_URL = os.getenv("CANVAS_URL")
ACCESS_TOKEN = os.getenv("CANVAS_ACCESS_TOKEN")
COURSE_ID = os.getenv("COURSE_ID")  # Replace with your course ID
ASSIGNMENT_ID = os.getenv("ASSIGNMENT_ID")  # Replace with your assignment ID

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


def update_grades(students):
    
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


