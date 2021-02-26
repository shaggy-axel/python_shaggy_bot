import json

json_str = '{ "name": "Max", "last_name": "Kainov", "age": 20 }'
json_str1 = '{ "name": "Max", "last_name": "Kainov"}'
json_str2 = '{ "name": "Max", "last_name": "Kainov", "emails": ["t@t.com", "y@y.com"] }'


print(type(json_str))
p1 = json.loads(json_str)
print(type(p1))
print(p1)

print(p1['name'])

# Превратить данные в экз класса

class Person:

	def __init__(self, **kwargs):
		for k, v in kwargs.items():
			setattr(self, k, v)


pr1 = Person(**json.loads(json_str))
print(type(pr1))
print(pr1.name)
print(pr1.age)

pr2 = Person(**json.loads(json_str2))
print(pr2.emails)

pr3 = Person(name='Test', some='What?')
print(pr3.some)
