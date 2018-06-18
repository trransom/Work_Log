#Work log
import os
import re

from task_screen import Task_Screen
from task import Task
from utils import Utils

def screen_prompt(display, input, regex):
	task = Task_Screen(display, input, regex)
	task.display()
	return task.input()

inpt = screen_prompt(
			'WORK LOG\nWhat would you like to do?\na) Add a new entry\nb) Search in existing entries\nc) Quit program', 
			'>', 
			'[AaBbCc]'
			)

if inpt.lower()=='a':
	#display the date task screen and retrieve the date.
	date = screen_prompt('Date of the task\nPlease use DD/MM/YYYY: ', '', '([0-3][0-9])\/([0-1][0-9])\/[0-9]{3}')
	
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
	if os.stat("log.csv").st_size == 0:
		util.write_header(util.filename, util.format, util.fieldnames)
	util.write_row(task.dictionary)
	
	#to press enter and to return to the main menu.
elif inpt.lower()=='b':
	options = screen_prompt('Do you want to search by:\na)Exact Date\n' +
							'b)Range of Dates\nc)Exact Search\nd)Regex Pattern\n' +
							'e)Return to Menu', '>', '[AaBbCcDdEe]')
	if options.lower()=='a':
		input = screen_prompt("Enter the date\nPlease use DD/MM/YYYY:", '>', '([0-3][0-9])\/([0-1][0-9])\/[0-9]{3}')
		file = open('log.csv', encoding='utf-8')
		data = file.read()
		i = 1
		list = re.findall(input, data)
		if list:
#			for item in list:
#				print(str(i) + '. ' + item + '\n')
#				i += 1
#			num = input('Which date would you like to look at? Please enter a number\n')
#			while num > len(list):
#				num = input('That number isn\'t on the list. Please try again\n')
			
		else: 
			print('No match')
elif inpt.lower()=='c':
	pass
