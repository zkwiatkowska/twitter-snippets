from collections import namedtuple

Person = namedtuple("Person", ["age", "name", "goal"])

zu = Person(age=26, name="Zuzanna", goal="Help people get into ML")

print(zu.age)   # 26
print(zu.name)  # Zuzanna
print(zu.goal)  # Help people get into ML
