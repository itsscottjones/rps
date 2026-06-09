import regex as re

def is_player_name_valid(name):
    return bool(re.search(r"^[a-zA-Z0-9 ]+$", name))

def name_cap(name):
    if name == "GLaDOS":
        return "GLaDOS"
    return name.capitalize()