import sys
import os

allowedlanguages = ["python"]

if (len(sys.argv) != 4):
    sys.exit("ERROR: requires argv: year numdays language")

year = sys.argv[1]
days = sys.argv[2]
language = sys.argv[3]

if language not in allowedlanguages:
    sys.exit("ERROR: allowed languages are: "+", ".join(allowedlanguages))

try:
    days = int(days)
except ValueError:
    sys.exit("ERROR: numdays needs to be a number")

for day in range(1,int(days)+1):
    os.system("python3 makeday.py "+year+" "+str(day)+" "+language)
