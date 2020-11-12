class Portfolio:
    def __init__(self):
        self.id = []
        self.positions = []

    def addPosition(self, position):
        if issubclass(type(position), Position):
            self.positions.append(position)
        else:
            print("not a position.")


class Position:
    def __init__(self):
        pass

    def timestep(self, jo):
        print(jo)


class Stock(Position):
    def __init__(self, name):
        self.name = name


class Realty(Position):
    def __init__(self):
        self.name = []
