# Use print("messages...") to debug your solution.

class Student:
	scores = [65,75,85,95]
	
	def average_score(self):
		total = 0
		for score in self.scores:
			total += score
		return total / len(self.scores)