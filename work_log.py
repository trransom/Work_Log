#Work log
import re

from task_screen import Task_Screen
from task import Task

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
	#to press enter and to return to the main menu.
elif inpt.lower()=='b':
	pass
elif inpt.lower()=='c':
	pass
