import csv
import os
import datetime
import time
from colorama import Fore, Back, Style
import tkinter as tk

os.system('clear')

oldfilename = input("Type the file name with path you want to separate.\n> ")
newfilename = input("Type the new file name with path you want to save.\n> ")
'''
mainWin = tk.Tk()
mainWin.title("CSV Separator")
mainWin.geometry('200x100')

filenameLabel = tk.Label(mainWin,text="Type the file name with path you want to separate.")
filenameLabel.pack()
filenameEntry = tk.Entry(mainWin,text="input")
filenameEntry.pack()

newfilenameLabel = tk.Label(mainWin,text="Type the new file name with path you want to save.")
newfilenameLabel.pack()
newfilenameEntry = tk.Entry(mainWin,text="input")
newfilenameEntry.pack()
'''
station = []
head = []
'''
oldfilename = filenameEntry.get()
print("[ " + Fore.GREEN + "Info" + Fore.RESET + " ] " + "old file name : " + oldfilename)
newfilename = newfilenameEntry.get()
print("[ " + Fore.GREEN + "Info" + Fore.RESET + " ] " + "new file name : " + newfilename)
'''

class Dataset:
	def __init__(self):
		self.__head = []
		self.__element_num = 0

	def createone(self, element):
		self.__head.append(element)

	def auto_create(self, element_num):
		self.__element_num = element_num
		for i in range(self.__element_num):
			i = []
			self.createone(i)
		return self.__head

begin = datetime.datetime.now()
with open(oldfilename) as csvfile:
	csvfile.seek(0)
	readcsv = csv.reader(csvfile, delimiter=',')
	iterator = 1

	for row in readcsv:
		iterator += 1
		temp = ''
		
		for matched in station:
			if matched == row[0]:
				temp = matched
				break
		if temp != row[0]:
			station.append(row[0])

	print("[ " + Fore.GREEN + "Info" + Fore.RESET + " ] " + "Loading files and setting up the service...")
	mydata = Dataset()
	mydata.__init__()
	#time.sleep(2)
	head = mydata.auto_create(len(station))

	for count in range(len(station)):
		csvfile.seek(0)
		for row in readcsv:
			if row[0] == station[count]:
				sublist = head[count]
				sublist.append(row)
		count += 1

	print("[ " + Fore.GREEN + "Info" + Fore.RESET + " ] " + "Total data's amounts is " + str(iterator))
	csvfile.close()

with open(newfilename, 'w') as csvfile:
	csvfile.seek(0)
	writecsv = csv.writer(csvfile, delimiter=',')
	print("[ " + Fore.GREEN + "Info" + Fore.RESET + " ] " + "Start to rewrite the datas!")
	#time.sleep(2)

	for first in range(len(station)):
		for second in range(len(head[first])):
			sta = head[first]
			writecsv.writerow(sta[second])

	csvfile.close()

end = datetime.datetime.now()
total_time_cost = end.second - begin.second
print("[ " + Fore.GREEN + "Info" + Fore.RESET + " ] " + "Total time cost = " + str(total_time_cost) + " s")

#mainWin.mainloop()
