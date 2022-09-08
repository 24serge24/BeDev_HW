hero = {"name" : "Abaddon",
		"characteristics" : {"level": "small",
							 "magic" : False,
							 "health" : 80,
							 "surveillance_range" : 350,
							 "delusion" : 45},
		"armor" : {"general_armor" : 4,
				   "armor_from_magic" : 2,
				   "armor_effects" : 3},
		"damage" : {"general_damage" : 8,
					"block_damage" : 4,
					"close_attack" : 9,
					"far_attack" : 4},
		"speed" : {"speed_of_movement" : 20,
				   "speed_turning" : 10,
				   "speed_battle" : 15},
				   }
hero["speed"]["speed_battle"] = 24 #тест зміна значення
speed_battle = hero.get("speed").get("speed_battle")
print(speed_battle)
hero["damage"]["distance_attack"] = 240 #тест + новий ключ змінна
distance_attack = hero.get("damage").get("distance_attack")
print(distance_attack)
del hero["armor"]["armor_effects"]
armor = hero.get("armor")
print(armor)
