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

    def getPerformance(self, start, end):
        performance = pd.DataFrame()
        for position in self.positions:
            performance = pd.concat(
                [performance, position.getPerformance(start, end)], axis=1)
            print(performance)
            # hier weiter, warum wird empty df returned
            # dann die tatsäclichen values und nicht den stockprice zurückgeben

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

    def getPerformance(self, start, end):
        raise NotImplementedError


class Stock(Position):
    def __init__(self, id, value, tradingFee=5):
        self.id = id
        self.value = value
        self.tradingFee = tradingFee

    def getPerformance(self, start, end):
        try:
            data = pdr.DataReader(self.id, data_source='iex',
                                  start=start, end=end)['Adj Close']
            data.index = pd.to_datetime(data.index)
        except:
            data = pdr.DataReader(self.id, data_source='yahoo',
                                  start=start, end=end)['Adj Close']
        return pd.DataFrame(data, columns=[self.id])

    def getDividends(self):
        pass


class Realty(Position):
    def __init__(self, id, value):
        self.id = id
        self.value = value
