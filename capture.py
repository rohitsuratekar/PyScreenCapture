"""
Rohit Suratekar (rohitsuratekar@gmail.com)
"""

import sys
import schedule
import time
import os
from PyQt4.QtGui import QPixmap, QApplication

#Settings

#This saves all screenshots in folder where script is running. Change this to path which you want to save. 
folder_path = os.path.dirname(os.path.abspath(__file__)) 

folder_name = "img" #This will create folder in which your screenshots will be stored
file_name_suffix = "screen"
every_seconds = 60#Time period between two screenshots (in seconds)
delay_between_frames = 1 #Time delay between two captures (in seconds, recommended : 1 sec)



app = QApplication(sys.argv)
#Create folder if not exists
os.makedirs(os.path.dirname('%s/%s/%s.png'%(folder_path, folder_name,  file_name_suffix)), exist_ok=True)
#First Screenshot
QPixmap.grabWindow(QApplication.desktop().winId()).save('%s/%s/%s0.png'%(folder_path,folder_name,  file_name_suffix), 'png')

class TakeScreenShot(object):
	"""Class to take screenshot"""
	current_file = 1
	def __init__(self):
		super(TakeScreenShot, self).__init__()

	def capture(self):
		QPixmap.grabWindow(QApplication.desktop().winId()).save('%s/%s/%s%d.png'%(folder_path,folder_name, file_name_suffix, self.current_file), 'png')
		print("Captured Image : %d" % self.current_file)
		self.current_file = self.current_file + 1

#Make only single instance so that we can modigy "current_file" inside itself 
current_instance = TakeScreenShot()

def job():
    current_instance.capture()

#Schedule job
schedule.every(every_seconds).seconds.do(job)

#Infinite loop. Close program to stop
while 1:
    schedule.run_pending()
    time.sleep(delay_between_frames)


		