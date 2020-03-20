#Central Logic for ELDROB project. Designed to be run on RPI 2B w/Arduino and Webcam
#By: Suhas Kanamarlapudi
#***DUE TO COVID 19 THIS PROGRAM IS INCOMPLETE AND CANNOT BE TESTED AND DEBUGGED W/O PROPER TEST HARDWARE. FULL PROGRAM IS EXPECTED TO BE COMPLETED ON APR 20

#Run central imports
import csv
import subprocess
from time import sleep
#Custom ArdCom Class **DUE TO COVID-19** THIS CLASS IS LACKING DEVELOPMENT HARDWARE FOR TESTING
#import ArdCom

#Setup NavMap (ArrayList style map)
Map1 = {'id': 0, "posx" : 0, "posy": 0}
Map2 = {'id': 1, "posx" : 0, "posy": 5}
Map3 = {'id': 2, "posx" : 0, "posy": 10}
Map4 = {'id': 3, "posx" : 5, "posy": 0}
Map5 = {'id': 4, "posx" : 10, "posy": 0}
Map6 = {'id': 5, "posx" : 5, "posy": 5}
Map7 = {'id': 6, "posx" : 5, "posy": 10}
Map8 = {'id': 7, "posx" : 10, "posy": 5}
Map9 = {'id': 8, "posx" : 10, "posy": 10}

#Define main pos_get()
def pos_get():
	navobj = subprocess.Popen("rm -r", cwd = "/home/pi/AprilNav-master/data")
	navobj = subprocess.Popen("./build/bin/AprilNav", cwd = "/home/pi/AprilNav-master")
	sleep(3) #Due to limited CPU and RAM on RPI2, a time buffer is required to let the values correctly calculate
	navobj.terminate()


def pos_cal():
	csvfile = open("/home/pi/AprilNav-master/data/positions.csv")
	parser = csv.reader(csvfile)

def pos_power():
	#Use Djikstra's Algorithm
	#Ardcom.implement(xpow,ypow)
	pass

def boilerplate():
	pos_get()
	pos_cal()
	pos_power()

#Recursively keep program running
intobj = boilerplate()
if intobj.text != "Complete. Terminate":
	intobj = boilerplate()