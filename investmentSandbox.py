import pandas as pd
import pandas_datareader as pdr


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
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def timestep(self, start, end):
        # get shareprice of startdate
        # get shareprice of enddate
        # calc change
        # update
        return start-end


class Realty(Position):
    def __init__(self, id, value):
        self.id = id
        self.value = value
