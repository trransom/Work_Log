#Work log
from task_screen import Task_Screen

t = 'WORK LOG\nWhat would you like to do?\na) Add a new entry\nb) Search in existing entries\nc) Quit program'
menu = Task_Screen(t, '>', ['A', 'a', 'B', 'b', 'C', 'c'])
menu.display()
inpt = menu.input()

if inpt.lower()=='a':
	print('Passed :)')
elif inpt.lower()=='b':
	pass
elif inpt.lower()=='c':
	pass