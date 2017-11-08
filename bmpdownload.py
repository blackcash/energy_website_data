#!/usr/bin/python
# coding=utf-8  

import requests
import shutil

class BmpDownload():

	def __init__(self):
		self.url = ''
		self.filename = ''

	def download(self):
		print(self.url,self.filename)
		res = requests.get(self.url , stream = True)
		f = open(self.filename,'wb')
		shutil.copyfileobj(res.raw,f)
		f.close()
		del res
	
	def setUrlAndFilename(self,url,filename):
		self.url = url
		self.filename = filename
		print(self.url,self.filename)
