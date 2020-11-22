import investmentSandbox as box

myPortfolio = box.Portfolio()
myPortfolio.addPosition(box.Stock('AAPL', 5000, '2015-1-1'))
myPortfolio.addPosition(box.Stock('SAP', 3500, '2015-1-1'))
myPortfolio.addPosition(box.Stock('VOW3.DE', 7000, '2015-1-1'))

print(myPortfolio.getPerformance('2015-1-10'))
# myPortfolio.plotPerformance(performance)

# hier weiter
# plotPerformance einbauen
# einbauen, dass man verschiedene investment dates eingeben kan
# get/print values einbauen
