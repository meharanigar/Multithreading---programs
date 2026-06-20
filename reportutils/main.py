import os
from  analyzer import (calculate_average,highest_mark,lowest_mark)
class FileNotFoundError(Exception):
     pass
try:
    file = "marks.txt"
    if not os.path.exists(file):
        raise FileNotFoundError("File not found")
    
    with open(file,"r") as file:
         marks = list(map(int,input().split()))
         file.read()
         
