import os
import subprocess
import sys
def printDisplay(word):
    os.chdir('/home/linaro/')
    process = subprocess.Popen(['sudo','./display.o',word],stdout=subprocess.PIPE)
    output,error = process.communicate()
