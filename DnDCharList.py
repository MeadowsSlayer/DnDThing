class Character:
	char_count = 0

	def start(self, char_name, char_specie, char_class, char_lvl):
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
			self.char_class = "Воин"
		elif int(char_class) == 5:
			self.char_class = "Паладин"
		elif int(char_class) == 6:
			self.char_class = "Монах"
		elif int(char_class) == 7:
			self.char_class = "Плут"
		elif int(char_class) == 8:
			self.char_class = "Следопыт"
		elif int(char_class) == 9:
			self.char_class = "Чародей"
		elif int(char_class) == 10:
			self.char_class = "Колдун"
		elif int(char_class) == 11:
			self.char_class = "Волшебник"
		elif int(char_class) == 12:
			self.char_class = "Друид"
		elif int(char_class) == 12:
			self.char_class = "Изобретатель"

		if int(char_lvl) > 20:
			self.__char_lvl = 20
		else:
			self.__char_lvl = char_lvl
		Character.char_count += 1

	def getlvl(self):
		print("Уровень персонажа:", self.__char_lvl, "\n")

	def setlvl(self, lvl):
		self.__char_lvl = lvl

charas = []
i = 0

while i != 1:
	name = input("Введите имя персонажа: ")
	specie = input("Введите число, соответствующее расе персонажа: \n 1 - человек, \n 2 - гном,\n 3 - драконорожденный,\n 4 - полуорк \nРаса: ")
	c_class = input("Введите число, соответствующее классу персонажа: \n 1 - варвар,\n 2 - бард,\n 3 - жрец,\n 4 - воин,\n 5 - паладин,\n 6 - монах,\n 7 - плут,\n 8 - следопыт,\n 9 - чародей,\n 10 - колдун,\n 11 - волшебник,\n 12 - друид,\n 13 - изобретатель \nКласс: ")
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

charas[0].setlvl(10)
charas[0].getlvl()