import requests

token = "5362955797:AAE6ykUZ2hv-Najtxl3EwuV8pnioGUgiTyg"
root_url = "https://api.telegram.org/bot"

ok_codes = 200, 201, 202, 203, 204

		
user = {"name" : "Serge",
    	"level" : "elementary",
		"id" : "24serge@gmail.com"
		}

message = {"user": user,
		   "message_text": message_text_next}
sentences = [{"texts": "My mum enjoys reading and my dad enjoys playing chess with my brother Ken. \nMy mum slim and is rather tall.", 
			  "level": "elementary"},
			  {"texts":"At my mother's long red hair and big brown eyes. \nShe has a very pleasant smile and a soft voice.", 
			  "level": "intermediate"},
			  {"texts":"My father is a doctor. \nHe is tall and handsome. \nHe has short dark hair and gray eyes.", 
			  "level": "advanced"},
			  {"texts":"My father  is a very hardworking man. \nHe is rather strict with us, \nbut always fair.", 
			  "level": "elementary"}
			]
			
def search_coincidences(message, sentences):
	translation_suggestions = []
	for sentence in sentences:
		if message.get("user").get("level") == sentence.get("level") and message.get("message_text") in sentence.get("texts"):
			translation_suggestions.append(sentence.get("texts"))
	return translation_suggestions
search = search_coincidences(message, sentences)

def options_result(translation):
	if len(translation) == 0:
		return("Нажаль немає жодних варiнтiв для перекладу.")
	if len(translation) == 1:
		return (translation[0])
	if len(translation) > 1:
		result_message = ""
		for x in translation:
			result_message += x + "\n ----- \n"
		return(result_message)

def get_bot_info(token):
	url = f"{root_url}{token}/getMe"
	response = requests.get(url)
	bot_info = response.json()
	return bot_info

def get_updates(token):
	url = f"{root_url}{token}/getUpdates"
	response = requests.get(url)
	updates = response.json()
	if response.status_code in ok_codes:
		result = {"error": None, "data": updates}
		return result
	else:
		result = {"error": "Bad code", "data": None}
		# print(f"Request failed with status: {response.status_code}")


def send_message(chat_id, message):
	url = f"{root_url}{token}/sendMessage"

	response = requests.post(url, json={'chat_id':chat_id, 'text': message})
	status = response.status_code
	
	if status != 200:
		print("Error message")
last_message_id = 0
while True:
	updates = get_updates(token)
	last_message = updates.get('data').get('result')[-1]
	chat_id = last_message.get('message').get('chat').get('id')
	message_text_next = last_message.get('message').get('text')
	message_text = options_result(search)
	#print(updates["data"]["result"])
	message_id =  last_message.get('message').get('message_id')
	
	if message_id > last_message_id:
		last_message_id = message_id
		send_message(chat_id, message_text)






