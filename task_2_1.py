translator = {"name" : None,
			  "level" : {"elementary"   : 1,
			  			 "intermediate" : 2,
			  			 "advanced"     : 3},
			  "entrance_language" : {"Ukraine" : "Ukr", #мова якою володіє користувач
			  						 "England" : "Eng",
			  						 "Poland"  : "Pl"},
			  "exit_language"     : {"Ukraine" : "Ukr", #мова якою хоче володіти користувач
			  						 "England" : "Eng",
			  						 "Poland"  : "Pl"},
			  "translator_type" : {"voice"  : "Voice", #користувачу надається можливість вводити текст з клавіатури або голосовими командами
			  					   "visual" : "Visual"},
			  "text" : {"elementary_text_1"   : "text_1_1", #пропозиції перекладу з випадаючого списку в залежновсті від рівня користувача
			  			"elementary_text_2"   : "text_1_2",
			  		    "intermediate_text_1" : "text_2_1",
			  			"intermediate_text_2" : "text_2_2",
			  			"intermediate_text_3" : "text_2_3",
					    "advanced_text_1"	  : "text_3_1",
			  			"advanced_text_1"	  : "text_3_2",
			  			"advanced_text_1"	  : "text_3_3",
			  			"advanced_text_1"	  : "text_3_4"},
			   "translation_style_1" : "colloquial", #користувавчу надається можливість вибору стилю перекладача (класичний, розмовний, інформаційний, науковий і т.д. )
			   "translation_style_2" : "conversational",
			   "translation_style_3" : "informational",
			   "translation_style_4" : "scientific",
			   "status_1" : "Certificate_elementary", #на виході сертифікат з відповідним рівнем знань
			   "status_2" : "Certificate_intermediate",
			   "status_3" : "Certificate_advanced",
			   }							   
print (translator["text"]["advanced_text_1"])

