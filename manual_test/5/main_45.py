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
fs.delete(None)


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

if all_objs.get(key_search) is None:
    print("State created just before delete should not be deleted \
        if delete has been called without object")
    exit(1)

print("OK", end="")
