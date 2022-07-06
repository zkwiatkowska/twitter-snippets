"""
Checking type of your variable in Python - type or isinstance? 🧐

*️⃣ "isinstance" includes inheritance. It means it can confirm that a model behaves not only like your ML model, but also ML model in general.

*️⃣ "type" can be used when checking if we have *exact* types match.
"""


class MLModel:
    pass


class MyAwesomeMLModel(MLModel):
    pass


my_awesome_model = MyAwesomeMLModel()

isinstance(my_awesome_model, MyAwesomeMLModel)      # True
isinstance(my_awesome_model, MLModel)               # True

type(my_awesome_model) == MyAwesomeMLModel          # True
type(my_awesome_model) == MLModel                   # False !!


