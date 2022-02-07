from Basic_Login import choose_course
from PyMemAPI import Course
from getpass import getpass
import json

if __name__ == "__main__":
    with open("account.env","r") as fp:
        js = json.load(fp)
        __username__ = js["USER"]
        __password__ = js["PASSWORD"]

    course: Course = choose_course(__username__, __password__)
    custom = {
        "1": "14092053",
        "5": "14092052",
    }
    status = course.move_level(103, 1, custom)
    if status:
        print("Success")
