#!/usr/bin/python3
""" Test
"""
from models.engine.file_storage import FileStorage
from models.state import State
import os


if os.path.exists(FileStorage._FileStorage__file_path):
    os.remove(FileStorage._FileStorage__file_path)


fs = FileStorage()

# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
key_search = "{}.{}".format("State", new_state.id)

# Delete nothing
fs.delete(new_state)


# All States
all_objs = fs.all()
try:
    all_objs.update(fs.all(State))
except:
    pass
try:
    all_objs.update(fs.all("State"))
except:
    pass

if all_objs.get(key_search) is not None:
    print("State created and deleted should not be in the list of objects")
    exit(1)

print("OK", end="")
