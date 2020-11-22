import datetime as dt

import pandas as pd
import pandas_datareader as pdr

import investmentSandbox_utils as utils


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

    def getPerformance(self, date):
        performance = pd.DataFrame()
        for position in self.positions:
            performance = pd.concat(
                [performance, position.getPerformance(date)], axis=1)
        return performance

    def getValue(self, date):
        value = pd.DataFrame()
        for position in self.positions:
            value = pd.concat(
                [value, position.getValue(date)], axis=1)
        return value

    def plotPerformance(self, start, end):
        pass
        # oder her in plot Klasse?
        # erstmal hier schreiben, später verschieben


class strategy:
    def __init__(self):
        self.id = []
        self.interval = []


class Position:
    def __init__(self):
        raise NotImplementedError

    def getPerformance(self, start, end):
        raise NotImplementedError

    def getValue(self, start, end):
        raise NotImplementedError


class Stock(Position):
    def __init__(self, id, investment, purchaseDate):
        self.id = id
        self.investment = investment
        self.purchaseDate = purchaseDate
        #self.tradingFee = []
        #self.taxation = []

    def getPerformance(self, date):
        date = utils.formatDate(date)
        try:
            data = pdr.DataReader(self.id, data_source='iex',
                                  start=self.purchaseDate, end=date)['Adj Close']
            data.index = pd.to_sdatetime(data.index)
        except:
            data = pdr.DataReader(self.id, data_source='yahoo',
                                  start=self.purchaseDate, end=date)['Adj Close']
        performance = pd.DataFrame(data)
        performance.columns = [self.id]
        return performance

    def getValue(self, date):
        performance = self.getPerformance(date)
        value = performance * self.investment
        return value

    def getDividends(self):
        pass


class Realty(Position):
    def __init__(self, id, value, purchaseDate):
        self.id = id
        self.value = value
        self.purchaseDate = purchaseDate

    def getPerformance(self, start, end):
        pass

    def getDividends(self):
        pass
