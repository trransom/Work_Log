#Work log
import csv
import os
import re
import sys

from datetime import datetime as dt
from task_screen import Task_Screen
from task import Task
from utils import Utils

def screen_prompt(display, input, regex):
	'''
		Displays a screen message and compares input
		against a regex pattern.
	'''
	task = Task_Screen(display, input, regex)
	task.display()
	return task.input()
	
def search_screen():
	options = screen_prompt('Do you want to search by:\na)Exact Date\n' +
							'b)Range of Dates\nc)Exact Search\nd)Regex Pattern\n' +
							'e)Return to Menu', '>', '[AaBbCcDdEe]')
	#Prompt for date search.
	if options.lower()=='a':
		inpt = screen_prompt("Enter the date\nPlease use MM/DD/YYYY:", '>', '([0-1][0-9])\/([0-3][0-9])\/[0-9]{4}')
		csv_file = csv.reader(open('log.csv', 'r+'), delimiter=',')#encoding='utf-8' 
		
		list = []
		for row in csv_file:
			if len(row)==0:
				continue
			elif inpt == row[0]:
				list.append(row)
		
		task_display(0, len(list), list)
	#prompt for range of dates
	elif options.lower()=='b':
		inpt = screen_prompt('Enter the range of dates.\nPlease use MM/DD/YYYY, MM/DD/YYYY format',
							'>', '([0-1][0-9])\/([0-3][0-9])\/[0-9]{4}, ([0-1][0-9])\/([0-3][0-9])\/[0-9]{4}')
		csv_file = csv.reader(open('log.csv', 'r+'), delimiter=',')
		
		inpt = inpt.split(', ')
		time1 = dt.strptime(inpt[0], '%m/%d/%Y')
		time2 = dt.strptime(inpt[1], '%m/%d/%Y')
		
		list = []
		for row in csv_file:
			if len(row)==0 or row[0]=='date':
				continue
			#The datetime stamp here might give us errors down the road. Just FYI, keep an eye on it.
			elif dt.strptime(row[0], '%m/%d/%Y') >= time1 and dt.strptime(row[0], '%m/%d/%Y') <= time2:
				list.append(row)
		
		if list:
			task_display(0, len(list), list)
		else:
			print('No matches found')
			
	#prompt for exact search
	elif options.lower()=='c':
		inpt = screen_prompt('Enter your exact search.\n', '>', '.*')
		csv_file = csv.reader(open('log.csv', 'r+'), delimiter=',')
		
		list = []
		for row in csv_file:
			if len(row)==0:
				continue
			else:
				for item in row:
					if item==inpt:
						list.append(row)
						continue
		if list:
			task_display(0, len(list), list)
		else:
			print('No matches found')
			
	elif options.lower()=='d':
		inpt = screen_prompt('Enter your regex pattern:\n', '>', '.*')
		csv_file = csv.reader(open('log.csv', 'r+'), delimiter=',')
		
		list = []
		for row in csv_file:
			if len(row)==0 or row[0]=='date':
				continue
			else:
				for item in row:
					if re.search(inpt, item):
						list.append(row)
						break
						
		if list:
			task_display(0, len(list), list)
		else:
			print('No matches found')
		
	elif options.lower()=='e':
		main()
		
def task_display(num1, total, list):
	'''
		Displays a single task and allows the user
		to cycle through a list of tasks.
	'''
	number = num1
	print('Date: ' + list[number][0] + '\n' +
			'Title: ' + list[number][1] + '\n' +
			'Time Spent: ' + list[number][2] + '\n' +
			'Notes: ' + list[number][3] + '\n\n' +
			'Result ' + str(number+1) + ' of ' + str(total) + '\n\n')
			
	ans = input('[N]ext, [B]ack, [R]eturn to search menu\n')
	if ans.lower()=='n' and number != total-1:
		task_display(number+1, total, list)
	elif ans.lower()=='b' and number !=0:
		task_display(number-1, total, list)
	elif ans.lower()=='r':
		search_screen()
	else:
		task_display(number, total, list)


def main():
	inpt = screen_prompt(
				'WORK LOG\nWhat would you like to do?\na) Add a new entry\nb) Search in existing entries\nc) Quit program', 
				'>', 
				'[AaBbCc]'
				)

	if inpt.lower()=='a':
		#display the date task screen and retrieve the date.
		date = screen_prompt('Date of the task\nPlease use MM/DD/YYYY: ', '', '([0-1][0-9])\/([0-3][0-9])\/[0-9]{4}')
		
		#Retrieve the title of the task
		name = screen_prompt('Name of the task: ', '>', '.*[\w\s].*')
		
		#Retrieve the time spent completing the task
		time = screen_prompt('Time Spent (rounded by minute): ', '>', '\d+')
		
		#Prompt for notes
		notes = screen_prompt('Notes (optional, allowed to leave blank): ', '>', '.*[\w\s].*')
		
		#Enter the task to the task log. Display a message prompting the user
		task = Task(date, name, time, notes)
		util = Utils('log.csv', 'a', ['date', 'name', 'time', 'notes'])
		
		#if log.csv is empty, write a header.
		try:
			if os.stat('log.csv').st_size == 0:
				util.write_header(util.filename, util.format, util.fieldnames)
		except FileNotFoundError:
			util.write_header(util.filename, util.format, util.fieldnames)
			
		util.write_row(task.dictionary)
		i = input('Task successfully logged. Press any key to return.\n')
		main()
		
		#to press enter and to return to the main menu.
		
	#Prompt user for type of search wanted
	elif inpt.lower()=='b':
		search_screen()

	elif inpt.lower()=='c':
		print('Thanks for using the Work Log program!')
		sys.exit()
	
	
main()