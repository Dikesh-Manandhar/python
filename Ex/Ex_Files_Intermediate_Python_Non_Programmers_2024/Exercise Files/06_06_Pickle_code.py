# Use print("messages...") to debug your solution.

import pickle

def depickle_to_string(pickled_data):
	the_string = ""
	
	word_list = pickle.loads(pickled_data)

	for x in range(0, len(word_list)):
		the_string += word_list[x]
		if x != len(word_list):
			the_string += " "

	return the_string
	
