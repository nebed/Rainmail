from GoogleScraper import scrape_with_config, GoogleSearchError
import os,sys
import subprocess
import glob
from os import path



def start_search(config):
	try:
		search = scrape_with_config(config)
	except GoogleSearchError as e:
		print(e)

#f = open('searchresultlinks.txt','w')    #indicate name of output file with google search links
#sys.stdout = f
#path= '/home/Desktop'
	for serp in search.serps:
	#print(serp)
		for link in serp.links:
		#print(link)
			print (link, f)  # or f.write('...\n')  print each link to the file
f.close()
