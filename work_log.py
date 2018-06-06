#Work log
import re

from task_screen import Task_Screen
from task import Task

t = 'WORK LOG\nWhat would you like to do?\na) Add a new entry\nb) Search in existing entries\nc) Quit program'
menu = Task_Screen(t, '>', 'a|b|c')
menu.display()
inpt = menu.input()

if inpt.lower()=='a':
	diff = Task_Screen('Date of the task\nPlease use DD/MM/YYYY: ', '', '(\d{2}|\d{1})\/(\d{2}|\d{1})\/\d{4}')
	diff.display()
	date = diff.input()
	print(date)
	#print('passed')
elif inpt.lower()=='b':
	pass
elif inpt.lower()=='c':
	pass