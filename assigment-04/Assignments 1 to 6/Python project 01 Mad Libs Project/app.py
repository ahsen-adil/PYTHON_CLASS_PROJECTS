
def madlib():
    # Collect user details
    name = input("What is your name? ")
    age = input("What is your age? ")
    github = input("What is your GitHub username? ")
    linkedin = input("What is your LinkedIn profile link? ")
    fav_language = input("What is your favorite programming language? ")
    fav_editor = input("What is your favorite code editor? ")

    # Craft the mad lib
    madlib = f"Meet {name}, a {age}-year-old passionate coder! When they're not busy exploring new \
repositories on GitHub ({github}), you can find them networking on LinkedIn ({linkedin}). {name} is \
a big fan of {fav_language}, and their favorite tool of choice is {fav_editor}. Whether they're debugging \
or writing clean code, {name} is always up for a challenge. Keep coding and creating magic, {name}!"

    print(madlib)

madlib()
