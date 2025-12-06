import sys
import os
from pathlib import Path
import shutil

allowedlanguages = ["python"]

if (len(sys.argv) != 4):
    sys.exit("ERROR: requires argv: year day language")

year = sys.argv[1]
day = sys.argv[2]
language = sys.argv[3]

if language not in allowedlanguages:
    sys.exit("ERROR: allowed languages are: "+", ".join(allowedlanguages))

cwd = os.getcwd()
if not os.path.exists(cwd+"/"+year):
    os.makedirs(cwd+"/"+year)
if not os.path.exists(cwd+"/"+year+"/"+day):
    os.makedirs(cwd+"/"+year+"/"+day)

Path(cwd+"/"+year+"/"+day+"/"+day+".in").touch()
Path(cwd+"/"+year+"/"+day+"/"+day+".test").touch()

if language == "python":
    if not os.path.exists(cwd+"/"+year+"/"+day+"/"+day+".py"):
        shutil.copyfile(cwd+"/template.py",cwd+"/"+year+"/"+day+"/"+day+".py")
    else:
        sys.exit("ERROR: "+cwd+"/"+year+"/"+day+"/"+day+".py already exists")
