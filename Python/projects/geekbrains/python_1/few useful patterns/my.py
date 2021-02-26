"""Игра лото"""
import random

NUMBERS = list(range(1, 91))


class Bag:
	"""Мешок с боченками"""

	def __init__(self):
		#Количество бочонков — 90 штук (с цифрами от 1 до 90)
		self._barrels = NUMBERS

	def shuffle(self):
		"""Трясем мешок"""
		random.shuffle(self._barrels)

	def pop(self):
		"""Достаем верхний боченок"""
		return self._barrels.pop()

	def __len__(self):
		return len(self._barrels)


class Card:
	"""Карточка лото"""

	def __init__(self):
		# берем 15 случайных чисел от 1 до 90
		numbers = random.sample(NUMBERS, 15)
		self._numbers = sorted(numbers) + sorted(numbers[5:10]) + sorted(numbers[10:])

	def cross_out(self, number):
		"""Зачеркнуть число"""
		self._numbers[self._numbers.index(number)] = '-'

	def __contains__(self, number):
		"""Поиск числа в карточке"""
		return number in self._numbers

	def is_empty(self):
		"""Мешок пуст"""
		return self._numbers.count('-') == 15


	def __str__(self):
		return """
			--------------------------
			    {} {} {}          {} {}
			 {}    {}    {} {}    {}
			   {} {} {}     {}      {}
			--------------------------
		""".format(*self._numbers)


class Player:
	"""Игрок компьютер"""

	def __init__(self, card, name):
		self.card = card
		self.name = name

	def is_winner(self):
		"""Игрок выиграл"""
		return self.card.is_empty()

	def turn(self, barrel):
		if barrel in self.card:
			self.card.cross_out(barrel)

		
if __name__ == "__main__":
	# для интереса пусть будет много (случайное кол-во игроков)
	player_number = random.randint(2, 8)
	print('Сегодня лото купили {} игроков!'.format(player_number))
	players = []
	for i in range(1, player_number):
		# создаем карточку
		car = Card()
		# создаем игрока
		player = Player(car, 'II-{}'.format(i))
		# добавляем в список игроков
		players.append(player)
	# создаем мешок
	bag = Bag()
	# не забываем потрясти его
	bag.shuffle()
	print('Мешок готов, начинаем!')
	is_winner = False
	# запускаем цикл игры до победы
	while not is_winner:
		# достаем боченок
		barrel = bag.pop()
		print('Боченок номер {}'.format(barrel))
		print('В мешке осталось {} боченков'.format(len(bag)))
		for player in players:
			player.turn(barrel)
			print('Карточка игрока {}:'.format(player.name))
			print(player.card)
			if player.is_winner():
				print('Победил {}. УРА!'.format(player.name))
				is_winner = True
				break

		