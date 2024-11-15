import requests

## dictionary of students and their addresses

with open('students.csv', 'r') as f:
    students = {}
    for line in f:
        name, address = line.split(',')
        students[name] = address

## dictionary of students and their grades
with open('grades.csv', 'r') as f:
    grades = {}
    for line in f:
        name, grade = line.split(',')
        grades[name] = grade


# Replace with your Canvas instance URL and API token
BASE_URL = "https://yourcanvasinstance.instructure.com/api/v1"
ACCESS_TOKEN = "your_access_token"

def update_grade(course_id, assignment_id, user_id, grade):
    url = f"{BASE_URL}/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}"
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


def grading():
    course_id = 12345
    assignment_id = 67890

    for student, address in students.items():
        grade = grades.get(student)
        if grade:
            user_id = address
            update_grade(course_id, assignment_id, user_id, grade)


## TODO: view the emitted events and update grades
