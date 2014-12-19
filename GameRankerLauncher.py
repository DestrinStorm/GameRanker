import sys
import os
import pickle
import time
import random
import xml.etree.ElementTree as etree
from urllib.request import urlopen
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from GameRanker import *

class MainForm(QMainWindow, Ui_GameRanker):

	NAME, MATCHES, POINTS, LSTREAK = range(4)
		
	def __init__(self,parent=None):
		super(MainForm, self).__init__(parent)
		self.ui=Ui_GameRanker()
		self.ui.setupUi(self)
		#Wire up the buttons
		self.ui.btnLoadData.clicked.connect(lambda: self.getCollection())
		self.ui.btnGame1.clicked.connect(lambda: winner(self.ui.txtGame1.toPlainText(),self.ui.txtGame2.toPlainText()))
		self.ui.btnGame2.clicked.connect(lambda: winner(self.ui.txtGame2.toPlainText(),self.ui.txtGame1.toPlainText()))
		
	def getCollection(self):
		downloadCollection(form)
		pairings(form)
		self.updateUI()
			
	def updateUI(self):
		nextPair(form)
		self.populateLists()

	def populateLists(self):             
		#populate main collection list
		form.ui.taCollection.clear()
		form.ui.taCollection.setSortingEnabled(False)
		headers = ["Name", "Matches", "Score", "LStreak"]
		form.ui.taCollection.setHorizontalHeaderLabels(headers)
		form.ui.taCollection.setRowCount(len(bgcollection))
		for row,boardgame in enumerate(bgcollection.keys()):
			#name column
			item = QTableWidgetItem(boardgame)
			form.ui.taCollection.setItem(row, self.NAME, item)
			#matches column
			item = QTableWidgetItem(str(bgcollection[boardgame]['matches']),2)
			form.ui.taCollection.setItem(row, self.MATCHES, item)
			#score column
			item = QTableWidgetItem(str(bgcollection[boardgame]['points']),2)
			form.ui.taCollection.setItem(row, self.POINTS, item)
			#lstreak column
			item = QTableWidgetItem(str(bgcollection[boardgame]['lstreak']),2)
			form.ui.taCollection.setItem(row, self.LSTREAK, item)
		form.ui.taCollection.setSortingEnabled(True)
		form.ui.taCollection.horizontalHeader().setSortIndicatorShown(False)
		form.ui.taCollection.sortItems(self.NAME)
		#populate collection ordered by score
		form.ui.taTop.clear()
		form.ui.taTop.setSortingEnabled(False)
		headers = ["Name", "Score"]
		form.ui.taTop.setHorizontalHeaderLabels(headers)
		form.ui.taTop.setRowCount(len(bgcollection))
		for row,boardgame in enumerate(bgcollection.keys()):
			#name column
			item = QTableWidgetItem(boardgame)
			form.ui.taTop.setItem(row, 0, item)
			#score column
			item = QTableWidgetItem(str(bgcollection[boardgame]['points']),2)
			form.ui.taTop.setItem(row, 1, item)
		form.ui.taTop.setSortingEnabled(True)
		form.ui.taTop.horizontalHeader().setSortIndicatorShown(False)
		form.ui.taTop.sortItems(1,Qt.DescendingOrder)
		form.ui.lcdCollection.display(form.ui.taCollection.rowCount())

#main execution starts here
#Initialisations - globalise bgcollection otherwise I can't modify it in the override loop
global bgcollection, matchpool, currentMatch
bgcollection = dict()
matchpool = []

#Define the DownloadCollection function
#Downloads data from BGG and pickles it to disk for later use by the loadCollection() function
def downloadCollection(parentwindow):
	#Initialisations
	parentwindow.ui.btnLoadData.setText("Connecting...")
	#ERROR HANDLING:
	username=parentwindow.ui.leUsername.text()
	minrating=parentwindow.ui.leMinRating.text()
	collection_url=("https://www.boardgamegeek.com/xmlapi2/collection?username="+username+"&minrating="+minrating+"&excludesubtype=boardgameexpansion&played=1&ff=1&subtype=boardgame")
	#Firstly, do an initial connection to start the collection cache process
	collectioncaching = 1
	while collectioncaching == 1:
		collection_probe = urlopen(collection_url)
		#check the HTTP return, 202 means we need to delay
		if collection_probe.getcode() == 202:
			#shut down, go to sleep for 30 secs
			parentwindow.ui.btnLoadData.setText("HTTP 202, sleeping for 30s...")
			collection_probe.close()
			time.sleep(30)
		else:
			collectioncaching = 0
	parentwindow.ui.btnLoadData.setText("Fetching...")
	#Right, press on with fetching the actual data now that BGG have it generated      
	#Fetch the 'want to play' collection XML, fill the objectiddict with it                
	with urlopen(collection_url) as collection_xml:
		collectiontree = etree.parse(collection_xml)
		collectionroot = collectiontree.getroot()
		#Stuff all those names into the list
		for each_child in collectionroot:
			bgcollection[each_child.find('name').text]={'matches':0, 'points':0, 'lstreak': 0}
	parentwindow.ui.btnLoadData.setText("Load Data")

def pairings(parentwindow):
	global currentMatch, matchpool
	#Pair up games into tournament brackets
	#first lets copy the games into a matchup list to pull from
	matchpool = list(bgcollection)
	#shuffle
	random.shuffle(matchpool)
	currentMatch = 1

def nextPair(parentwindow):
	global currentMatch
	parentwindow.ui.txtGame1.setPlainText(matchpool[(currentMatch*2)-2])
	parentwindow.ui.txtGame2.setPlainText(matchpool[(currentMatch*2)-1])
	#Is this the last pairing?
	if (len(matchpool) - currentMatch*2) <= 1:
		pairings(form)
	else:
		currentMatch = currentMatch+1

def winner(winninggame,losinggame):
	global bgcollection, currentMatch
	bgcollection[winninggame]['matches'] = bgcollection[winninggame]['matches']+1
	bgcollection[losinggame]['matches'] = bgcollection[losinggame]['matches']+1
	bgcollection[winninggame]['points'] = bgcollection[winninggame]['points']+1
	bgcollection[winninggame]['lstreak'] = 0
	bgcollection[losinggame]['lstreak'] = bgcollection[losinggame]['lstreak']+1
	if bgcollection[losinggame]['lstreak'] == 5:
		del bgcollection[losinggame]
	form.updateUI()
	
if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = MainForm()
	form.show()
	sys.exit(app.exec_())
