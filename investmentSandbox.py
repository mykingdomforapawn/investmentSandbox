import pandas as pd
import pandas_datareader as pdr


class Portfolio:
    """ lffgef """

    def __init__(self):
        """
        Beschreibung:
        Params: 
        """
        self.id = []
        self.positions = []
        self.strategy = []

    def addPosition(self, position):
        if issubclass(type(position), Position):
            self.positions.append(position)
        else:
            print("not a position.")

    def calcDiversification(self, start, end):
        sum = []
        for position in self.positions:
            sum = sum + position.getValue(end) - position.getData(start)

    def calcPerformance(self, start, end):
        for position in self.positions:
            data = position.getData(start, end)
            # erst zu df machen
            # dann concat, worin das andere berechnet wird

            performance = pd.DataFrame(
                [data, data/data[0] * position.value], columns=['First Name', 'sec'])
            print(performance)
            # zeitreihe aktienwert dem output hinzufügen
            # no normieren, dass startwert = 1
            # normierte reihe mal positionswert
            # diese reihe auch dem output hinzufügen

    def plotPerformance(self, start, end):
        pass
        # oder her in plot Klasse?
        # klingt besser


class strategy:
    def __init__(self):
        self.id = []
        self.interval = []


class Position:
    def __init__(self):
        raise NotImplementedError

    def getData(self, start, end):
        raise NotImplementedError


class Stock(Position):
    def __init__(self, id, value, tradingFee=5):
        self.id = id
        self.value = value
        self.tradingFee = tradingFee

    def getData(self, start, end):
        try:
            data = pdr.DataReader(self.id, data_source='iex',
                                  start=start, end=end)['Adj Close']
            data.index = pd.to_datetime(data.index)
        except:
            data = pdr.DataReader(self.id, data_source='yahoo',
                                  start=start, end=end)['Adj Close']
        return data

    def getDividends(self):
        pass


class Realty(Position):
    def __init__(self, id, value):
        self.id = id
        self.value = value
