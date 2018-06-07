#Utils
import csv

class Utils():
	
	def __init__(self, dictionary={}):
		self.dictionary = dictionary
		
	def print_dict(csv, num1, num2):
		'''
			Print all of the rows in the csv file by
			converting them to a dictionary format.
		'''
		with open(csv, newline='') as csvfile:
			dictreader = csv.DictReader(csvfile, delimter='|')
			rows = list(dictreader)
			for row in rows[num1:num2]:
				print(row)
				
	def search_dict():
		'''
			
		'''
		pass
		
	def dates_list():
		pass
		
	def log_task(task):
		'''
			Add a task to the log file.
		'''
		pass
		
	