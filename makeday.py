import sys
import os
from pathlib import Path
import shutil

year = sys.argv[1]
day = sys.argv[2]
language = sys.argv[3]


cwd = os.getcwd()
if not os.path.exists(cwd+"/"+year):
    os.makedirs(cwd+"/"+year)
if not os.path.exists(cwd+"/"+year+"/"+day):
    os.makedirs(cwd+"/"+year+"/"+day)

Path(cwd+"/"+year+"/"+day+"/"+day+".in").touch()
Path(cwd+"/"+year+"/"+day+"/"+day+".test").touch()

if language == "python":
    shutil.copyfile(cwd+"/template.py",cwd+"/"+year+"/"+day+"/"+day+".py")
