import json
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

student = {
    "name": "Avinash",
    "age": 22,
    "skills": ["Python", "SQL", "Git"]
}

try:
    with open("student.json", "w") as file:
        json.dump(student, file, indent=4)

    logging.info("Student data saved successfully")

except OSError as error:
    logging.error("Failed to save student data: %s", error)