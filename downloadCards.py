import os
from requests import get
#Pokemon TCG API
from pokemontcgsdk import Card
from pokemontcgsdk import Set 

class PKMNDownloader():

	def __init__(self):

		self.imgPath = "Z:/Python/img/cards/"

	def makeFolder(self, path):
	  	try:
	  		os.makedirs(path)

	  	except OSError:
	  		pass

	def download(self, url, file_name):
	    # open in binary mode
	    with open(file_name, "wb") as file:
	        # get request
	        response = get(url)
	        # write to file
	        file.write(response.content)

	def getSets(self, sets):

		for s in sets:

			setPath = self.imgPath + s.code

			self.makeFolder(setPath)	
			#download logo
			url = s.logo_url
			fileName = setPath + "/logo.png"
			self.download(url, fileName)
			#download set symbol
			url = s.symbol_url
			fileName = setPath + "/symbol.png"
			self.download(url, fileName)

			self.getCards(s.code, s.total_cards)

	def getCards(self, code, count):

		cards = Card.where(setCode=code, pageSize=count)

		print(len(cards))

		for c in cards:
			url = c.image_url
			fileName = "Z:/Python/img/cards/" + code + "/" + c.number + ".png"
			print(fileName)
			self.download(url, fileName)

if __name__ == '__main__':
    downloader = PKMNDownloader()
    sets = Set.where(standardLegal=False,expandedLegal=True)
    downloader.getSets(sets)