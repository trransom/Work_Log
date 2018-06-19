#Work log
import csv
import os
import re
import sys

from task_screen import Task_Screen
from task import Task
from utils import Utils

def screen_prompt(display, input, regex):
	task = Task_Screen(display, input, regex)
	task.display()
	return task.input()
	
def task_display(num1, total):
	number = num1
	print('Date: ' + list[number][0] + '\n' +
			'Title: ' + list[number][1] + '\n' +
			'Time Spent: ' + list[number][2] + '\n' +
			'Notes: ' + list[number][3] + '\n\n' +
			'Result ' + str(number+1) + ' of ' + str(total) + '\n\n')
	ans = input('[N]ext, [E]dit, [D]elete, [R]eturn to search menu')
	if ans.lower()=='n' and number != total-1:
		task_display(number+1, total)
	else:
		task_display(number, total)

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
	try:
		if os.stat('log.csv').st_size == 0:
			util.write_header(util.filename, util.format, util.fieldnames)
	except FileNotFoundError:
		util.write_header(util.filename, util.format, util.fieldnames)
		
	util.write_row(task.dictionary)
	
	#to press enter and to return to the main menu.
elif inpt.lower()=='b':
	options = screen_prompt('Do you want to search by:\na)Exact Date\n' +
							'b)Range of Dates\nc)Exact Search\nd)Regex Pattern\n' +
							'e)Return to Menu', '>', '[AaBbCcDdEe]')
	if options.lower()=='a':
		inpt = screen_prompt("Enter the date\nPlease use DD/MM/YYYY:", '>', '([0-3][0-9])\/([0-1][0-9])\/[0-9]{3}')
		csv_file = csv.reader(open('log.csv', 'r+'), delimiter=',')#encoding='utf-8' 
		
		list = []
		for row in csv_file:
			if len(row)==0:
				continue
			elif inpt == row[0]:
				list.append(row)
		
		task_display(0, len(list))
		

elif inpt.lower()=='c':
	pass
