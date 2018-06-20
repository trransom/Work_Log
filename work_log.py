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
	
def list_search(list):
	if list:
		task_display(0, len(list), list)
	else: 
		ans = input('No results found. Press any key to return to the search menu.\n')
		search_screen()
	
def search_screen():
	'''
		Displays the menu for choosing which searching
		method you want to use, Exact Date, Range of Dates,
		Exact Search, Regex Pattern, or to return to the
		menu.
	'''
	os.system('cls')
	options = screen_prompt('Do you want to search by:\na)Exact Date\n' +
							'b)Range of Dates\nc)Exact Search\nd)Regex Pattern\n' +
							'e)Return to Menu', '>', '[AaBbCcDdEe]')
	#Prompt for date search.
	if options.lower()=='a':
		os.system('cls')
		inpt = screen_prompt("Enter the date\nPlease use MM/DD/YYYY:", '>', '([0-1][0-9])\/([0-3][0-9])\/[0-9]{4}')
		csv_file = csv.reader(open('log.csv', 'r+'), delimiter=',')#encoding='utf-8' 
		
		#cycle through rows, adding matches to list as they are found
		list = []
		for row in csv_file:
			if len(row)==0:
				continue
			elif inpt == row[0]:
				list.append(row)
		list_search(list)
	#prompt for range of dates
	elif options.lower()=='b':
		os.system('cls')
		inpt = screen_prompt('Enter the range of dates.\nPlease use MM/DD/YYYY, MM/DD/YYYY format',
							'>', '([0-1][0-9])\/([0-3][0-9])\/[0-9]{4}, ([0-1][0-9])\/([0-3][0-9])\/[0-9]{4}')
		csv_file = csv.reader(open('log.csv', 'r+'), delimiter=',')
		
		inpt = inpt.split(', ')
		time1 = dt.strptime(inpt[0], '%m/%d/%Y')
		time2 = dt.strptime(inpt[1], '%m/%d/%Y')
		
		#cycle through rows, converting every date into a datetime for comparison.
		list = []
		for row in csv_file:
			if len(row)==0 or row[0]=='date':
				continue
			elif dt.strptime(row[0], '%m/%d/%Y') >= time1 and dt.strptime(row[0], '%m/%d/%Y') <= time2:
				list.append(row)
		
		list_search(list)
			
	#prompt for exact search
	elif options.lower()=='c':
		os.system('cls')
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
		list_search(list)
			
	elif options.lower()=='d':
		os.system('cls')
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
						
		list_search(list)
		
	elif options.lower()=='e':
		main()
		
def task_display(num1, total, list):
	'''
		Displays a single task and allows the user
		to cycle through a list of tasks.
	'''
	os.system('cls')
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
	'''
		Displays the main menu and prompts
		user for a choice to either add a task, 
		search for a task, or to exit the program.
	'''
	os.system('cls')
	inpt = screen_prompt(
				'WORK LOG\nWhat would you like to do?\na) Add a new entry\nb) Search in existing entries\nc) Quit program', 
				'>', 
				'[AaBbCc]'
				)

	if inpt.lower()=='a':
		os.system('cls')
		#display the date task screen and retrieve the date.
		date = screen_prompt('Date of the task\nPlease use MM/DD/YYYY: ', '', '([0-1][0-9])\/([0-3][0-9])\/[0-9]{4}')
		
		os.system('cls')
		#Retrieve the title of the task
		name = screen_prompt('Name of the task: ', '>', '.*[\w\s].*')
		
		os.system('cls')
		#Retrieve the time spent completing the task
		time = screen_prompt('Time Spent (rounded by minute): ', '>', '\d+')
		
		os.system('cls')
		#Prompt for notes
		notes = screen_prompt('Notes (optional, allowed to leave blank): ', '>', '.*[\w\s].*')
		
		os.system('cls')
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
		os.system('cls')
		i = input('Task successfully logged. Press any key to return.\n')
		main()
		
		
		
	#Prompt user for type of search wanted
	elif inpt.lower()=='b':
		search_screen()

	#Exit the program
	elif inpt.lower()=='c':
		os.system('cls')
		print('Thanks for using the Work Log program!')
		sys.exit()
	
main()
