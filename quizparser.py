import json
import urllib.request

url = "https://apis.getmindmap.com/api/story/quizResponse/5170A"

def downloadJSON(link):
	"""Downloads and parses a JSON from the specified link"""
	with urllib.request.urlopen(link) as url:
		data = url.read().decode()
		return json.loads(data)

json = downloadJSON(url)

#Quiz Data
quizID = json["_id"]
quizResponses = [] # [quiz_id, response, id, date]

#Quiz Responses
for quiz in json["quiz_response"]:
	quizResponses.append( [quiz["quiz_id"], quiz["response"], quiz["_id"], quiz["date"]] )

#Sort responses
quizResponses = sorted(quizResponses, key = lambda x: x[0])
for count, quiz in enumerate(quizResponses, 1):
	quiz[0] = count

#Save info
with open(quizID + ".csv", "w") as file:
	for quiz in quizResponses:
		file.write("{0},{1},{2},{3}\n".format(quiz[0], quiz[1], quiz[2], quiz[3]))

print("Finished processing {0} quizzes".format(len(quizResponses)))
print("Saved to file " + quizID + ".csv")
