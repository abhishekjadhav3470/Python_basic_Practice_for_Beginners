import os, sys 
from os.path import dirname, join, abspath


sys.path.insert(0, abspath(join(dirname(__file__), "..")))
# the above is written to clear all the path to the proper file for the function

from course import course_details

def payment():
    print("this is my payment file")

course_details.course()