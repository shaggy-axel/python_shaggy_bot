def my_simple_decorator(function_to_decorate):

	def wrapper_around_our_function():
		#Внутри себя декроратор определяет функцию обертку,
		# Она будет обернута вокруг декорируемой
		# получая возможность исполнять произвольный код до и после

		print('I am code, which will have completed before completing of function_to_decorate')

		function_to_decorate()

		print('I am code, which will have completed after completing of function_to_decorate')

	return wrapper_around_our_function()

def stable_function():
	print('Hello World!')
stable_function_decorated = my_simple_decorator(stable_function)

print(stable_function_decorated)