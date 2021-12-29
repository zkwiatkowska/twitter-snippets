class MLModel:
    pass


class MyAwesomeMLModel(MLModel):
    pass


my_awesome_model = MyAwesomeMLModel()

isinstance(my_awesome_model, MyAwesomeMLModel)  # True
isinstance(my_awesome_model, MLModel)  # True

type(my_awesome_model) == MyAwesomeMLModel  # True
type(my_awesome_model) == MLModel  # False !!


