#Task object

class Task():

	def __init__(self, date, title, time_spent, notes):
		self.date = date
		self.title = title
		self.time_spent = time_spent
		self.notes = notes
		self.dictionary = {'date': self.date, 'name': self.title, 'time': self.time_spent, 'notes': self.notes}