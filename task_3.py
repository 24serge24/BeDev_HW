print ("Привiт, як тебе звати?")
user = {"name" : input (),
    	"level" : ["elementary", "intermediate", "advanced"],
		"entrance_language" : ["Ukraine", "England", "Poland"], #мова якою володіє користувач
		"exit_language"     : ["Ukraine", "England", "Poland"],  #мова якою хоче володіти користувач
		}
print (user["name"] + " введiть мову яку ви бажаєте вивчати та рiвень знань.")
# дальще через випадаючу строку вибираєм рівень і т.д.(ми ще це не вивчали)
elementary_text_ukr_1   = ["text_eng_1_1", "text_eng_1_2"] #пропозиції перекладу з випадаючого списку в залежновсті від рівня користувача
intermediate_text_ukr_1 = ["text_eng_2_1", "text_eng_2_2", "text_eng_2_3"]
advanced_text_ukr_1     = ["text_eng_3_1", "text_eng_3_2", "text_eng_3_3", "text_eng_3_4"] # і т.д.. Я докінця не розумію, ми варіанти перекладу будем прописувати вручну чи вони будуть підтягуватись з бази?
text = [elementary_text_ukr_1, intermediate_text_ukr_1, advanced_text_ukr_1]
#print (user["exit_language"][1])
#print (text[2][3])

