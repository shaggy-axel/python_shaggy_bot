numbers = range(1, 20)


class UnforunedNumberError(Exception):

	def __init__(self, number):
		self.number = number
		super().__init__()

	def __str__(self):
		return 'Несчастливое число {}'.format(self.number)
		

class UnforunedNumberChinaError(UnforunedNumberError):

	def __str__(self):
		return 'Несчастливое число в Китае {}'.format(self.number)
		


for i in numbers:
	try:
		if i in (4, 13):
			if i == 4:
				raise UnforunedNumberChinaError(i)
			else:
				raise UnforunedNumberError(i)
		else:
			print(i)
	except UnforunedNumberChinaError as e:
		print(e)
	except UnforunedNumberError as e:
		print(e)
	except Exception:
		print('Какая то неизвестная ошибка')
