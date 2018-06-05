#Task Screen
import os
import re

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
			if re.match(self.answers, ans):
				print('Please enter a valid entry.')
				continue
			else:
				return ans
				