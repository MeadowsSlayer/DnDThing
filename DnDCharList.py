charas = []

class Character:
	char_count = 0

	def start(self, char_name, char_specie, char_class, char_lvl, char_stats, char_hp = 0):
		print("||Персонаж создан||", "\n")

		self.stats = [0, 0, 0, 0, 0, 0]
		self.modyfiers = [0, 0, 0, 0, 0, 0]

		#Раса персонажа
		self.char_name = char_name

		if int(char_specie) == 1:
			self.char_specie = "Человек"
		elif int(char_specie) == 2:
			self.char_specie = "Дварф"
		elif int(char_specie) == 3:
			self.char_specie = "Полурослик"
		elif int(char_specie) == 4:
			self.char_specie = "Эльф"
		elif int(char_specie) == 5:
			self.char_specie = "Драконорожденный"
		elif int(char_specie) == 6:
			self.char_specie = "Гном"
		elif int(char_specie) == 7:
			self.char_specie = "Полуорк"
		elif int(char_specie) == 8:
			self.char_specie = "Тифлинг"
		elif int(char_specie) == 9:
			self.char_specie = "Полуэльф"

		#Класс персонажа
		if int(char_class) == 1:
			self.char_class = "Варвар"
		elif int(char_class) == 2:
			self.char_class = "Бард"
		elif int(char_class) == 3:
			self.char_class = "Жрец"
		elif int(char_class) == 4:
			self.char_class = "Монах"
		elif int(char_class) == 5:
			self.char_class = "Плут"
		elif int(char_class) == 6:
			self.char_class = "Колдун"
		elif int(char_class) == 7:
			self.char_class = "Друид"
		elif int(char_class) == 8:
			self.char_class = "Изобретатель"
		elif int(char_class) == 9:
			self.char_class = "Чародей"
		elif int(char_class) == 10:
			self.char_class = "Волшебник"
		elif int(char_class) == 11:
			self.char_class = "Воин"
		elif int(char_class) == 12:
			self.char_class = "Паладин"
		elif int(char_class) == 13:
			self.char_class = "Следопыт"

		self.char_class_num = int(char_class)

		#Задаем уровень в пределах от 1 до 20
		if int(char_lvl) > 20:
			self.__char_lvl = 20
		elif int(char_lvl) < 1:
			self.__char_lvl = 1
		else:
			self.__char_lvl = int(char_lvl)

		#Раздаем статы и приписываем к ним модификаторы
		for i in range(6):
			for c in range(len(char_stats)):
				if (char_stats[c] == " ") and (len(char_stats) >= 2):
					self.stat = int(char_stats[:c])
					char_stats = char_stats[c+1:]
					break
			self.stats[i] = self.stat

		for i in range(6):
			if (self.stats[i] == 1):
				self.modyfiers[i] = -5
			elif (self.stats[i] == 2) or (self.stats[i] == 3):
				self.modyfiers[i] = -4
			elif (self.stats[i] == 4) or (self.stats[i] == 5):
				self.modyfiers[i] = -3
			elif (self.stats[i] == 6) or (self.stats[i] == 7):
				self.modyfiers[i] = -2
			elif (self.stats[i] == 8) or (self.stats[i] == 9):
				self.modyfiers[i] = -1
			elif (self.stats[i] == 10) or (self.stats[i] == 11):
				self.modyfiers[i] = 0
			elif (self.stats[i] == 12) or (self.stats[i] == 13):
				self.modyfiers[i] = 1
			elif (self.stats[i] == 14) or (self.stats[i] == 15):
				self.modyfiers[i] = 2
			elif (self.stats[i] == 16) or (self.stats[i] == 17):
				self.modyfiers[i] = 3
			elif (self.stats[i] == 18) or (self.stats[i] == 19):
				self.modyfiers[i] = 4
			elif (self.stats[i] == 20):
				self.modyfiers[i] = 5

		#Задаем хиты в зависимости от класса и уровня
		if int(char_class) == 1:
			self.char_hp = 12 + ((self.__char_lvl - 1) * 7) + (self.__char_lvl * self.modyfiers[2])

		elif (int(char_class) >= 2) and (int(char_class) <= 8):
			self.char_hp = 8 + ((self.__char_lvl - 1) * 5) + (self.__char_lvl * self.modyfiers[2])

		elif (int(char_class) >= 9) and (int(char_class) <= 10):
			self.char_hp = 6 + ((self.__char_lvl - 1) * 4) + (self.__char_lvl * self.modyfiers[2])

		elif int(char_class) >= 11:
			self.char_hp = 10 + ((self.__char_lvl - 1) * 6) + (self.__char_lvl * self.modyfiers[2])

		#Отслеживаем число персонажей
		Character.char_count += 1

	def getstats(self):
		print("STR:", self.stats[0], " (", self.modyfiers[0], ")")
		print("DEX:", self.stats[1], " (", self.modyfiers[1], ")")
		print("CON:", self.stats[2], " (", self.modyfiers[2], ")")
		print("INT:", self.stats[3], " (", self.modyfiers[3], ")")
		print("WIS:", self.stats[4], " (", self.modyfiers[4], ")")
		print("CHA:", self.stats[5], " (", self.modyfiers[5], ")")

	def getlvl(self):
		print("Уровень персонажа", self.char_name, "-", self.__char_lvl)

	def setlvl(self, lvl):
		self.__char_lvl = lvl
		if int(self.char_class_num) == 1:
			self.char_hp = 12 + ((self.__char_lvl - 1) * 7) + (self.__char_lvl * self.modyfiers[2])

		elif (int(self.char_class_num) >= 2) and (int(self.char_class_num) <= 8):
			self.char_hp = 8 + ((self.__char_lvl - 1) * 5) + (self.__char_lvl * self.modyfiers[2])

		elif (int(self.char_class_num) >= 9) and (int(self.char_class_num) <= 10):
			self.char_hp = 6 + ((self.__char_lvl - 1) * 4) + (self.__char_lvl * self.modyfiers[2])

		elif int(self.char_class_num) >= 11:
			self.char_hp = 10 + ((self.__char_lvl - 1) * 6) + (self.__char_lvl * self.modyfiers[2])


def Menu():
	option = input("1 - Создать нового персонажа\n2 - Просмотреть список созданных персонажей\n3 - Закрыть программу\n")
	if int(option) == 1:
		print(" ")
		CharacterCreation()
	elif int(option) == 2:
		print(" ")
		LookForChara()

def CharacterCreation():
	name = input("Введите имя персонажа: ")
	specie = input("Введите число, соответствующее расе персонажа: \n 1 - человек, \n 2 - дварф,\n 3 - полурослик,\n 4 - эльф,\n 5 - драконорожденный,\n 6 - гном,\n 7 - полуорк,\n 8 - тифлинг,\n 9 - полуэльф \nРаса: ")
	c_class = input("""Введите число, соответствующее классу персонажа: \n 1 - варвар,\n 2 - бард,
		\n 3 - жрец,\n 4 - монах,\n 5 - плут,\n 6 - колдун,\n 7 - друид,\n 8 - изобретатель,\n 9 - чародей,
		\n 10 - волшебник,\n 11 - воин,\n 12 - паладин,\n 13 - следопыт \nКласс: """)
	level = input("Введите уровень персонажа: ")
	statistics = input("Введите характеристики через пробел(только численные значения): ")
	statistics = statistics + " "
	charas.append(Character())
	count = Character.char_count
	charas[count].start(name, specie, c_class, level, statistics)
	print("Число персонажей: ", Character.char_count, "\n")

	Menu()

def LookForChara():
	for i in range(Character.char_count):
		print(i, "-", charas[i].char_name)
	name_of_chara = input("Выберите персонажа: ")
	print(" ")

	print("Имя персонажа:", charas[int(name_of_chara)].char_name)
	print("Раса персонажа:", charas[int(name_of_chara)].char_specie)
	print("Класс персонажа:", charas[int(name_of_chara)].char_class)
	charas[int(name_of_chara)].getlvl()
	print("Хиты персонажа:", charas[int(name_of_chara)].char_hp)
	print("Характеристики персонажа: ")
	charas[int(name_of_chara)].getstats()

	Menu()

Menu()