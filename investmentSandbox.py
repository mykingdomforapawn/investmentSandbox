class portfolio:
    def __init__(self):
        self.stockPositions = []
        self.realtyPositions = []

    def addPosition(self, position):
        self.stockPositions.append(position)


class position:
    def __init__(self):
        pass

    def timestep(self, jo):
        print(jo)


class stock(position):
    def __init__(self, name):
        self.name = name


class realty:
    def __init__(self):
        self.name = []
