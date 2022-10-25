class Dog:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def get_name(self):
		return self.name

d = Dog("Tim",34)
print(d.get_name())
d2 = Dog("Bill",12)
print(d2.get_name())