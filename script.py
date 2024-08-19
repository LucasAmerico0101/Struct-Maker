#program that creates simple web project structure
from maker import *
from os import path
import os
project_name  = input("Input the project name: ")
maker.construct(project_name)