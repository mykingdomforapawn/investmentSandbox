import pandas_datareader as pdr

import investmentSandbox as box

myPortfolio = box.Portfolio()
myPortfolio.addPosition(box.Stock("AAPL", 23, 4))
#myPortfolio.addPosition(box.Stock("SAP", 10, 4))
#myPortfolio.addPosition(box.Stock("MSFT", 34, 4))

myPortfolio.getPerformance('2015-1-1', '2015-1-10')
# myPortfolio.regroupPositions(exampleInput)

#data = myPosition.getData('2015-1-1', '2015-1-2')

# myPortfolio.addPosition(myPosition)
# myPortfolio.addPosition("this")

# print(myPortfolio.positions)

# aapl = pdr.DataReader("AAPL",
#                     start = '2015-1-1',
#                     end = '2015-1-2',
#                     data_source = 'yahoo')['Adj Close']
# print(aapl)
# pdr.DataReader(self.id, 'iex', self.start, self.end)
