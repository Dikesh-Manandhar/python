# Use print("messages...") to debug your solution.

import json

thestr = """
{
	"title":"Intermediate Python",
	"students": [
		{
			"name":"Nick",
			"scores": [
				56,
				73,
				68,
				84
			]
		},
		{
			"name":"Jane",
			"scores": [
				88,
				74,
				91,
				73
			]
		},
		{
			"name":"Mark",
			"scores": [
				93,
				66,
				52,
				33
			]
		}
	]
}
"""
json_course_data = json.loads(thestr)

def get_scores():
	first_test_scores = []
	for student in json_course_data["students"]:
		first_test_scores.append(student["scores"][0])
	return first_test_scores
	
