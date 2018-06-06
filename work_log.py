#Work log
import re

from task_screen import Task_Screen
from task import Task

t = 'WORK LOG\nWhat would you like to do?\na) Add a new entry\nb) Search in existing entries\nc) Quit program'
menu = Task_Screen(t, '>', '[AaBbCc]')
menu.display()
inpt = menu.input()

if inpt.lower()=='a':
	#display the date task screen and retrieve the date.
	task = Task_Screen('Date of the task\nPlease use DD/MM/YYYY: ', '', '([0-3][0-9])\/([0-1][0-9])\/[0-9]{3}')
	task.display()
	date = task.input()
	print(date)
	
	#Retrieve the title of the task
	
	#Retrieve the time spent completing the task
	
	#Prompt for notes
	
	#Enter the task to the task log. Display a message prompting the user
	#to press enter and to return to the main menu.
elif inpt.lower()=='b':
	pass
elif inpt.lower()=='c':
	pass
