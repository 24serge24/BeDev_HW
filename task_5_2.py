print ("Привiт, як тебе звати?")
user = {"name" : input (),
    	"level" : "elementary",
		"id" : "24serge@gmail.com"
		}
print (user.get("name") + " введiть текст для подальших варiнтiв перекладу..")
message = {"user": user,
		   "message_text": input ()}
sentences = [{"texts": "My mum enjoys reading and my dad enjoys playing chess with my brother Ken. \n My mum slim and is rather tall.", 
			  "level": "elementary"},
			  {"texts":"At my mother's long red hair and big brown eyes. \n She has a very pleasant smile and a soft voice.", 
			  "level": "intermediate"},
			  {"texts":"My father is a doctor. \n He is tall and handsome. \n He has short dark hair and gray eyes.", 
			  "level": "advanced"},
			  {"texts":"My father  is a very hardworking man. \n He is rather strict with us, \n but always fair.", 
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
		for x in translation:
			translation  += x
		print(translation)
options_result(search)
"""	
if not matched_sentences:
    result_message = "None result"
if len(matched_sentences) == 1:
    result_message = matched_sentences[0]
if len(matched_sentences) > 1:
		for x in matched_sentences:
			matched_sentences += x + "\n...\n"		

"""

