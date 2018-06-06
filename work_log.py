#Work log
import re

from task_screen import Task_Screen
from task import Task

t = 'WORK LOG\nWhat would you like to do?\na) Add a new entry\nb) Search in existing entries\nc) Quit program'
menu = Task_Screen(t, '>', '[AaBbCc]')
menu.display()
inpt = menu.input()

if inpt.lower()=='a':
	diff = Task_Screen('Date of the task\nPlease use DD/MM/YYYY: ', '', '([0-3][0-9])\/([0-1][0-9])\/[0-9]{3}')
	diff.display()
	date = diff.input()
	print(date)
	#print('passed')
elif inpt.lower()=='b':
	pass
elif inpt.lower()=='c':
	pass
