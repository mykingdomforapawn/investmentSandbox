import investmentSandbox as box

myPortfolio = box.portfolio()
myPosition = box.stock("AAPL")

print(myPortfolio.stockPositions)
myPortfolio.addPosition(myPosition)
print(myPortfolio.stockPositions)

# print(myPortfolio)

#myPosition = box.stock("AAPL")


# print(myPosition)
# print(myPosition.name)
# print(myPosition.timestep("hi"))
