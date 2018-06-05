#Task Screen
import os

class Task_Screen():

	def __init__(self, display_message, answers):
		self.display_message = display_message
		self.answers = answers
		
	def display(self):
		os.system('cls')
		print(self.display_message)
		

	
	def main_menu(self):
		answers = ['a', 'b', 'c']
	
		print('WORK LOG\nWhat would you like to do?\na) Add a new entry\nb) Search in existing entries\nc) Quit program')
		while True:
			ans = input('>')
			try:
				value = ans.lower()
			except ValueError:
				print('Please enter a valid letter.')
				continue
			if value in answers:
				break
			else:
				print('Please enter a valid letter')
				