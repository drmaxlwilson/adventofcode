import sys
import os

year = sys.argv[1]
days = sys.argv[2]
language = sys.argv[3]

for day in range(1,int(days)+1):
    os.system("python3 makeday.py "+year+" "+str(day)+" "+language)
