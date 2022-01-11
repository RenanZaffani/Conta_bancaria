
class Client:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("Show: @property name()")
        return self.__name.tittle()

    @name.setter
    def name(self, name):
        print("Show: setter name()")
        self.__name = name
