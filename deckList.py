import sys
#Pokemon TCG API
from pokemontcgsdk import Card
from pokemontcgsdk import Set

class Deck():

	def __init__(self, path):

		self.cardData = self.loadFile(path)
		self.deckList = self.buildList(self.cardData)

	def progressBar(self, value, endvalue, bar_length=20):

		percent = float(value) / endvalue
		arrow = '-' * int(round(percent * bar_length)-1) + '>'
		spaces = ' ' * (bar_length - len(arrow))

		sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
		sys.stdout.flush()

	def loadFile(self, path):

		f = open(path,'r')
		i = 0
		data = []
		while True:
			text = f.readline()
			if '******' in text:
				i = i + 1
				if i is 2:
					break
			elif '* ' in text :
				arr = text.split(' ')
				size = len(arr)
				# Count , PTCGOCode, Number
				data.append([arr[1], arr[size - 2], arr[size - 1]])
		return data

	def getPaths(self, root = "img/cards/"):

		paths = []

		for item in self.deckList:
			paths.append(root + item.card.set_code + '/' + item.card.number + '.png')

		return paths



	def buildList(self, cardData):

		deckList = []

		i = 0

		print("Loading Card Data:")
		self.progressBar(i, len(cardData))

		for d in cardData:
			class Item(object):
				pass

			item = Item()

			item.count = int(d[0])

			if d[1] is "" or "Energy" in d[1]:

				code = "sm1"

				print(d[2])

				item.card = Card.find(code + "-" + str(int(d[2])+163))

			else:
				
				code = Set.where(ptcgoCode=d[1])[0].code

				item.card = Card.find(code + "-" + d[2])

			deckList.append(item)

			i = i + 1

			self.progressBar(i, len(cardData))

			

		return deckList

if __name__ == '__main__':
	Deck("Z:/Python/deckLists/Trinity.txt")