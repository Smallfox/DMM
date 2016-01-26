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
	lower = 325
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
	

print "Start to download Image..."
print "Please Select download method (1)For automatic loop (2)For your input:"
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
else:
	print "Invaild option."
print "All completed."
