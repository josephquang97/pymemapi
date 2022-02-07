from PyMemAPI import Memrise

def choose_course(__username__,__password__):
    # Sign in Memrise
    user = Memrise()
    user.login(__username__, __password__)

    # Choose the course
    course = user.select_course()
    return course