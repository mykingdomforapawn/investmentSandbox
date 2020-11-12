import investmentSandbox as box

myPortfolio = box.Portfolio()
myPosition = box.Stock("AAPL", 23)

myPortfolio.addPosition(myPosition)
myPortfolio.addPosition("this")

print(myPortfolio.positions)

# print(myPortfolio)

#myPosition = box.stock("AAPL")


# print(myPosition)
# print(myPosition.name)
# print(myPosition.timestep("hi"))
