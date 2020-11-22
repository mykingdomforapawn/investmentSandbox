import datetime as dt

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import seaborn as sns

import investmentSandbox_utils as utils


class Portfolio:
    """ lffgef """

    def __init__(self):

        self.id = []
        self.positions = []
        self.strategy = []

    def addPosition(self, position):
        """Add a position object to this portfolio.

        Args:
            position (Position): the number to get the square root of.
        Returns:
            none
        Raises:
            TypeError: if position is not a position object.

        """

        if issubclass(type(position), Position):
            self.positions.append(position)
        else:
            raise TypeError(
                "Input has wrong data type. (req. Position object) ")

    def getPerformance(self, date):
        """Get the performance of all positions in portfolio.

        Args:
            date (str): end date for performance data output.
        Returns:
            performance (DataFrame): daily performance of positions.
        Raises:
            TypeError: if date is not a str.
            ValueError: if date is outside of boundaries.

        """

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

    def plotPerformance(self, performance):
        # Data
        # höhe der tab als x werte
        # spalten als numpy arrays umwandeln
        # xticklabels mit den labes der tab audffüllen
        # benennung nach den Spaltennamen

        x = range(1, 6)
        y = [[1, 4, 6, 8, 9], [2, 2, 7, 10, 12], [2, 8, 5, 10, 6]]

        # Plot
        plt.stackplot(x, y, labels=['A', 'B', 'C'])
        plt.legend(loc='upper left')
        plt.show()

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
