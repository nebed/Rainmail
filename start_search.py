from GoogleScraper import scrape_with_config, GoogleSearchError
import os,sys
import subprocess
import glob
from os import path



def start_search(config):
	urls_to_process = deque([ ])
	try:
		search = scrape_with_config(config)
	except GoogleSearchError as e:
		print(e)

	for serp in search.serps:
		print(serp)

		for link in serp.links:
			url = str(link)
			urls_to_process = urls_to_process.append(url)

