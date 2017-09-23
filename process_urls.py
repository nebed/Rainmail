from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re

def process_urls(urls_to_process):

	processed_urls = set()  # a set of urls that have already been crawled
	emails = set()  # a set of extracted emails

	while len(urls_to_process) > 0:  # process urls one by one until we exhaust the queue

		url = urls_to_process.popleft()  # move next url from the queue to the set of processed urls
		processed_urls.add(url)
		parts = urlsplit(url)    # extract base url to resolve relative links
		base_url = "{0.scheme}://{0.netloc}".format(parts)
		path = url[:url.rfind('/')+1] if '/' in parts.path else url
		print("Processing %s" % url)
		try:
			response = requests.get(url)
		except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
		# ignore pages with errors
			continue

		new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))   # extract all email addresses and add them into a set
		emails.update(new_emails)
		soup = BeautifulSoup(response.text)     # create a beutiful soup for the html document

		for anchor in soup.find_all("a"):
			link = anchor.attrs["href"] if "href" in anchor.attrs else ''  # extract link url from the anchor

			if link.startswith('/'):   # resolve relative links
				link = base_url + link

			elif not link.startswith('http'):
				link = path + link

			if not link in urls_to_process and not link in processed_urls:   # add the new url to the queue if it was not enqueued nor processed yet
				urls_to_process.append(link)
	return emails
