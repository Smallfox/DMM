#
#Downloader for Imma Devil Carnival - 300,360,500,510 series
#after downloading complete, cropped and make gif 
#
import os
import urllib
import array
import numpy
import sys
import StringIO
from PIL import Image
from images2gif import writeGif

#2016/9/11 add
def ichaDownloadAll():
	url_prefix = "http://157.7.147.219/icha/"
	url_postfix = "/images/_"
	imageType = ".png"
	for i in range(100,1000,3):
		for j in range(1,4,1):
			downloadStr = url_prefix + "360"+ str(i) + url_postfix + str(j) + imageType
			urllib.urlretrieve(downloadStr , "360" + str(i) + "-" + str(j) + imageType)
			print downloadStr + " donwloaded. \n"

def imageDowload(head):
	head = head.rstrip('\n')
	url_prefix = "http://157.7.147.219/img/anime2/sm_99_"
	sean = "_sean2_"
	imageType = ".jpg"
	for i in range(10,100,4):
		for j in range(1,4,1):
			urllib.urlretrieve(url_prefix + head + str(0) + str(i) + sean + str(j) + imageType, head + str(0) + str(i) + str(j) + imageType)
		print "Image Number:" + head + str(0) + str(i) + " downloaded."
		pasteImage(head + str(0) + str(i))
	for i in range(100,1000,4):
		for j in range(1,4,1):
			urllib.urlretrieve(url_prefix + head + str(i) + sean + str(j) + imageType, head + str(i) + str(j) + imageType)
		print "Image Number:" + head + str(i) + " downloaded."
		pasteImage(head + str(i) )
	return

def makeImage2Gif(seanName, imgType):
	img = Image.open(seanName + imgType)
	lower = 345
	upper = 0
	box = (0, upper, 460, lower)
	gifarray = []
	for i in range(1,49,1):
		img.crop(box).save(seanName + str(i) + imgType)
		gifarray.append(seanName + str(i) + imgType)
		upper = upper + 345
		lower = lower + 345
		box = (0, upper, 460, lower)
	gifarray = numpy.array(gifarray)
	buf = buffer(gifarray)
	writeGif(seanName + "-004" + ".gif", buf, duration=0.05, repeat=True)
	print "gif " + seanName + " created."
	for i in range(1,49,1):
		os.remove(seanName + str(i) + imgType)
	print "Clear clipped Image."
	return;

def pasteImage(fileserialname):
	mergedimg = Image.new('RGBA', (460, 16560))
	for i in range(1,4,1):
		floatimg = Image.open(fileserialname + str(i) + ".jpg")
		mergedimg.paste(floatimg, (0,5520*(i-1)) )
	mergedimg.save(fileserialname + ".jpg")
	print "Image " + fileserialname +  " concantenation completed"
	makeImage2Gif(fileserialname, ".jpg")
	return;

def userInputImage(imageserial):
	url_prefix = "http://157.7.147.219/img/anime2/sm_99_"
	sean = "_sean2_"
	imgtype = ".jpg"
	imageserial = imageserial.rstrip('\n')
	for i in range(1,4,1):
		urllib.urlretrieve(url_prefix + imageserial + sean + str(i) + imgtype, imageserial + str(i) + imgtype )
	pasteImage(imageserial)
	return;

def downloadSerailImage(imageNumber):
	card_prefix = "http;//157.7.147.219/img/card/de_card_e_"
	anime_prefix = "http://157.7.147.219/img/anime2/sm_99_"
	sean = "_sean"
	imageNumber = imageNumber.rstrip('\n')
	#for i in range(1,4,1):
	#	urllib.urlretrieve(card_prefix + imageNumber + 
	urllib.urlretrieve(anime_prefix + imageNumber + sean + "1.jpg", imageNumber + "-003.jpg") 
	urllib.urlretrieve(anime_prefix + imageNumber + sean + "3.jpg", imageNumber + "-005.jpg") 
	print "\nComplete"
	return;

print "Start to download Image..."
print "Please Select download method (1)For automatic loop (2)For your input (3)Downlaod Card (4)icha download:"
option = sys.stdin.readline()
always = ""

if option.rstrip('\n') == "1":
	print "Input the head name:"
	topName = sys.stdin.readline()
	imageDowload(topName)
elif option.rstrip('\n') == '2':
	while always.rstrip('\n') != "2":
		print "Please Enter the image name:"
		imgName = sys.stdin.readline()
		userInputImage(imgName)
		print "Continue(1) or leave(2)..."
		always = sys.stdin.readline()

elif option.rstrip('\n') == '3':
	print "Input the card name:"
	cardName = sys.stdin.readline()
	downloadSerailImage(cardName)

elif option.rstrip('\n') == '4':
	print "Auto Downloading..."
	ichaDownloadAll()

else:
	print "Invaild option."
print "All completed."
