import os

from PIL import Image, ImageFilter


class ImageManger():

	#def __init__(self, path):

	def makeFolder(self, path):
	  	try:
	  		os.makedirs(path)

	  	except OSError:
	  		pass

	def getFolders(self):

		class Folder(object):
			pass

		arr = []

		directory = os.fsencode('img/cards/')

		for subDir in os.listdir(directory):
			if os.path.isdir(os.path.join(directory, subDir)): 
				folder = Folder()
				folder.name = os.fsdecode(subDir)
				folder.dir = os.path.join(directory, subDir)
				arr.append(folder)
				continue
			else:
				continue

		return arr

	def getPaths(self, folder):

		arr = []

		for imgFile in os.listdir(folder.dir):

			filename = os.fsdecode(imgFile)

			if (filename.endswith(".png") and 
					("logo" not in filename) and 
					("symbol" not in filename)):

				self.makeFolder('img/crop/'+ folder.name + '/')

				arr.append(('img/cards/' + folder.name + '/' + filename, 
						'img/crop/'+ folder.name + '/' + filename))

		return arr

	def cropImage(self, path, y):

		#Read image
		im = Image.open(path)

		#Applying a filter to the image
		im_sharp = im.filter( ImageFilter.SHARPEN )

		#crop image
		#245 x 342
		width, height = im.size
		left = int(width * (22/float(245)))
		top = int(height * (y/float(342)))
		right = int(width * (223/float(245)))
		bottom = int(height * ((y+108)/float(342)))

		im_crop = im.crop((left, top, right, bottom))

		return im_crop

	def cropAll(self):
		for folder in self.getFolders():
			for filePath, savePath in self.getPaths(folder):
				crop = self.cropImage(filePath, 42)
				crop.save(savePath, "PNG")


if __name__ == '__main__':
	manager = ImageManger()
	manager.cropAll()
	for num in range(164,173,1):
		filePath, savePath = ('img/cards/sm1/' + str(num) + '.png','img/crop/sm1/' + str(num) + '.png')
		crop = manager.cropImage(filePath,118)
		crop.save(savePath, "PNG")


