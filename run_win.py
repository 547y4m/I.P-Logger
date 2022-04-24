import os
import subprocess
import time
import platform
from pyfiglet import Figlet

custom_fig = Figlet(font='graffiti')
ascii_banner = custom_fig.figlet_format("Tracker")
print(ascii_banner)
print("=================================By-547y4m. (Updated by shasankp000")
print(f"Detected OS : {platform.platform()}")
print(f"Detected python version : {platform.python_version()}")





curn_dir = os.getcwd()
print(curn_dir)
os.chdir(r"{}".format(curn_dir))
print("Generating ngrok link......in 20 secs.")
print("Using this link one can access the webpage")
print("And to exit just press the exit button, idk why but CTRL+C isn't gonna work....*shrugs*")
print("Hope you have read this by now, link will appear anytime now...it ends with an 'ngrok.io'")
time.sleep(20)
subprocess.Popen("run_ngrok.bat")
print("Deploying flask app.....")
time.sleep(10)
subprocess.Popen("run.bat")
