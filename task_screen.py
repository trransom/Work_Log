#Task Screen

class Task_Screen():
	
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
				