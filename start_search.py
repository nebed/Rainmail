from GoogleScraper import scrape_with_config, GoogleSearchError
import os,sys
import subprocess
import glob
from os import path



#function to perform search based on input configuration

def start_search(config):
	urls_to_process = deque()
	try:
		search = scrape_with_config(config)
	except GoogleSearchError as e:
		print(e)

	for serp in search.serps:
		print(serp)

		for link in serp.links:
			print(link)
			retrieved_url = str(link)
			end = len(retrieved_url) -1
			urls_to_process.append(retrieved_url[25:end])
	return urls_to_process
