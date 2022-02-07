import logging
import json
from PyMemAPI import Course, Memrise

def choose_course(username: str, password: str) -> Course:
    # Sign in Memrise
    user = Memrise()
    user.login(username, password)

    # Choose the course
    course: Course = user.select_course()
    return course

if __name__ == "__main__":
    with open("account.env","r") as fp:
        js = json.load(fp)
        __username__ = js["USER"]
        __password__ = js["PASSWORD"]

    course: Course = choose_course(__username__, __password__)
    levels = course.levels()
    for level in levels:
        words = level.get_words()
        for word in words:
            try:
                response = word.update_ipa('fr')
            except:
                logging.warning(f"Fail to update IPA word \"{word.text}\"")