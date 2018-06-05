#Task Screen
import os

class Task_Screen():

	def __init__(self, display_message, input_prompt, answers):
		self.display_message = display_message
		self.input_prompt = input_prompt
		self.answers = answers
		
	def display(self):
		os.system('cls')
		print(self.display_message)
		

	def input(self):
		while True:
			ans = input(self.input_prompt + '')
			if ans not in self.answers:
				print('Please enter a valid entry.')
				continue
			else:
				return ans
				
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
				