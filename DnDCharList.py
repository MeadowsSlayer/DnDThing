class Character:
	char_count = 0

	def start(self, char_name, char_specie, char_class, char_lvl, char_hp = 0):
		print("||Персонаж создан||", "\n")

		#Раса персонажа
		self.char_name = char_name
		if int(char_specie) == 1:
			self.char_specie = "Человек"
		elif int(char_specie) == 2:
			self.char_specie = "Гном"
		elif int(char_specie) == 3:
			self.char_specie = "Драконорожденный"
		elif int(char_specie) == 4:
			self.char_specie = "Полуорк"

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

		if int(char_class) == 1:
			self.char_hp = 12 + ((self.__char_lvl - 1) * 7)

		elif (int(char_class) >= 2) and (int(char_class) <= 8):
			self.char_hp = 12 + ((self.__char_lvl - 1) * 5)

		elif (int(char_class) >= 9) and (int(char_class) <= 10):
			self.char_hp = 12 + ((self.__char_lvl - 1) * 4)

		elif int(char_class) >= 11:
			self.char_hp = 12 + ((self.__char_lvl - 1) * 6)

		#Отслеживаем число персонажей
		Character.char_count += 1

	def getlvl(self):
		print("Новый уровень персонажа", self.char_name, "-", self.__char_lvl)

	def setlvl(self, lvl):
		self.__char_lvl = lvl
		if int(self.char_class_num) == 1:
			self.char_hp = 12 + ((self.__char_lvl - 1) * 7)

		elif (int(self.char_class_num) >= 2) and (int(self.char_class_num) <= 8):
			self.char_hp = 12 + ((self.__char_lvl - 1) * 5)

		elif (int(self.char_class_num) >= 9) and (int(self.char_class_num) <= 10):
			self.char_hp = 12 + ((self.__char_lvl - 1) * 4)

		elif int(self.char_class_num) >= 11:
			self.char_hp = 12 + ((self.__char_lvl - 1) * 6)

charas = []
i = 0

while i != 1:
	name = input("Введите имя персонажа: ")
	specie = input("Введите число, соответствующее расе персонажа: \n 1 - человек, \n 2 - гном,\n 3 - драконорожденный,\n 4 - полуорк \nРаса: ")
	c_class = input("Введите число, соответствующее классу персонажа: \n 1 - варвар,\n 2 - бард,\n 3 - жрец,\n 4 - монах,\n 5 - плут,\n 6 - колдун,\n 7 - друид,\n 8 - изобретатель,\n 9 - чародей,\n 10 - волшебник,\n 11 - воин,\n 12 - паладин,\n 13 - следопыт \nКласс: ")
	level = input("Введите уровень персонажа: ")
	charas.append(Character())
	count = Character.char_count
	charas[count].start(name, specie, c_class, level)

	i = input("Если вы хотите создать еще персонажа, то введите 0, если же с вас достаточно, вы устали и весь мир остановился - введите 1: \n")
	i = int(i)

print("Число персонажей: ", Character.char_count, "\n")

for i in range(Character.char_count):
	print("Имя персонажа:", charas[i].char_name)
	print("Раса персонажа:", charas[i].char_specie)
	print("Класс персонажа:", charas[i].char_class)
	charas[i].getlvl()
	print("Хиты персонажа:", charas[i].char_hp)
	print("")

charas[0].setlvl(10)
charas[0].getlvl()
print("Хиты персонажа:", charas[0].char_hp)