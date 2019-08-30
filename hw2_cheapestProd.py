#!/usr/bin/python

"""HW#2: String Manipulation
Programming in Business. Mark, a businessman would like to purchase commodities
necessary for his own sari-sari store. He would like to determine what commodity is the
cheapest one for each type of products. You will help Mark by creating a program that
processes a list of five strings. The format will be the name of the commodity plus its
price(<name>-<price>)."""

commodityList = ["Sensodyne-100,Close Up-150, Colgate-135",
"Safeguard-80, Protex-50, Kojic-135",
"Surf-280, Ariel-350, Tide-635",
"Clover-60, Piatos-20, Chippy-35",
"Jelly bean-60, Hany-20, Starr-35"]
print("Commodity list = ", commodityList,"\n")

tpasteCateg = commodityList[0].split(',')
soapCateg = commodityList[1].split(',')
dgentCateg = commodityList[2].split(',')
chipsCateg = commodityList[3].split(',')
candiesCateg = commodityList[4].split(',')

tpastePrice = [int(x.split('-')[1]) for x in tpasteCateg]
cheapTpaste = tpasteCateg[tpastePrice.index(min(tpastePrice))]

soapPrice = [int(x.split('-')[1]) for x in soapCateg]
cheapSoap = soapCateg[soapPrice.index(min(soapPrice))]

dgentPrice = [int(x.split('-')[1]) for x in dgentCateg]
cheapDgent = dgentCateg[dgentPrice.index(min(dgentPrice))]

chipsPrice = [int(x.split('-')[1]) for x in chipsCateg]
cheapChips = chipsCateg[chipsPrice.index(min(chipsPrice))]

candiesPrice = [int(x.split('-')[1]) for x in candiesCateg]
cheapCandies = candiesCateg[candiesPrice.index(min(candiesPrice))]

totalCheapPrice = min(tpastePrice) + min(soapPrice) + min(dgentPrice) + min(chipsPrice) + min(candiesPrice)
print("Cheapest: %s,%s,%s,%s,%s" %(cheapTpaste,cheapSoap,cheapDgent,cheapChips,cheapCandies))
print("Total:", totalCheapPrice)