#Utils
import csv

class Utils():

	def __init__(self, filename, format, fieldnames):
		'''
			Initializes a Utils object by declaring the
			filename, the format, and the fieldnames.
		'''
		self.filename = filename
		self.format = format
		self.fieldnames = fieldnames

	def write_header(self, filename, format, fieldnames):
		'''
			Writes a header to the specified file with the
			given fieldnames.
		'''
		with open(filename, format) as csvfile:
			self.writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			self.writer.writeheader()
		
	def write_row(self, dictionary):
		'''
			Writes a row of data to the specified
			csv file.
		'''
		with open(self.filename, 'a', newline='') as csvfile:
			self.writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
			self.writer.writerow(dictionary)
		
	def print_dict(csv, num1, num2):
		'''
			Prints all of the rows in the csv file by
			converting them to a dictionary format.
		'''
		with open(csv, newline='') as csvfile:
			dictreader = csv.DictReader(csvfile, delimter='|')
			rows = list(dictreader)
			for row in rows[num1:num2]:
				print(row)
				