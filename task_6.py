print ("Привiт, як тебе звати?")
user = {"name" : input (),
    	"level" : "elementary",
		"id" : "24serge@gmail.com"
		}
print (user.get("name") + " введiть текст для подальших варiнтiв перекладу..")
message = {"user": user,
		   "message_text": input ()}
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
		print("Нажаль немає жодних варiнтiв для перекладу.")
	if len(translation) == 1:
		print (translation[0])
	if len(translation) > 1:
		result_message = ""
		for x in translation:
			result_message += x + "\n ----- \n"
		print(result_message)
options_result(search)
# Мабуть доцільно ці дві функції обєднати, проте я хотів спробувати щоб функція викликала іншу функцію.

