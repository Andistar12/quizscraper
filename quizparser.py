import json
import urllib.request
import csv
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def downloadJSON(link):
	"""Downloads and parses a JSON from the specified link"""
	with urllib.request.urlopen(link) as url:
		data = url.read().decode()
		return json.loads(data)

def process_quizjson(json):
	"""Processes one quiz JSON"""
	#Quiz Data
	quizID = json["_id"]
	quizResponses = [] # [quiz_id, response, id, date]

	#Quiz Responses
	for quiz in json["quiz_response"]:
		quizResponses.append( [quiz["quiz_id"], quiz["response"], quiz["_id"], quiz["date"]] )

	#Responses & recode quiz_id
	for count, quiz in enumerate(quizResponses, 1):
		quiz[0] = count

	#Save info
	with open(quizID + ".csv", "w") as ourfile:
		field_names = ["quiz_id", "response", "id", "date"]
		writer = csv.DictWriter(ourfile, fieldnames = field_names)
		writer.writeheader()
	
		for quiz in quizResponses:
			writer.writerow({
				"quiz_id": quiz[0],
				"response": quiz[1],
				"id": quiz[2],
				"date": quiz[3]
			})
			
	print("Saved {0} quizzes to file {1}.csv".format(len(quizResponses), quizID))



#Add URLs to this as needed
urls = ["https://apis.getmindmap.com/api/story/quizResponse/5170A"]

for entry in urls:
	gottenJson = downloadJSON(entry)
	process_quizjson(gottenJson)
