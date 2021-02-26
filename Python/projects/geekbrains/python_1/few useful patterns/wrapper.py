# 

class PrivateException(Exception):
	
	def __init__(self, attrname, class_name):
		self.attrname = attrname
		self.class_name = class_name

	def __str__(self):
		return '{}.{} is private!'.format(self.class_name, self.attrname)
		

class NoIncWrapped:
	def __init__(self, wrapped):
		self.wrapped = wrapped
		
	def __getattr__(self, attrname):
		if attrname.startswith('_'):
			raise PrivateException(attrname, self.__class__.__name__)
		else:
			return getattr(self.wrapped, attrname)


class NoInc:

	def __init__(self, a, b):
		"""Инициализатор: a-это будет число"""
		self.a = a
		self._b = b
		self.__f = 56

	def __private(self):
		print("Это приватный метод!")


n = NoInc(10, 20)
n = NoIncWrapped(n)
#print(n._b)
print(n.a)
#n._NoInc__private()
#print(n._NoInc__f)
