#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from GoogleScraper import scrape_with_config, GoogleSearchError
import os,sys
import subprocess
import glob
from os import path
from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re



countrycodes = [ 'AD','AE','AF','AG','AL','AM','AO','AQ','AR','AS','AT','AU','AZ','BA','BB','BD','BE','BF','BG','BH','BI','BJ','BN','BO','BQ','BR','BS','BT','BW','BY','BZ','CA','CC','CD','CF','CG','CH','CI','CK','CL','CM','CN','CO','CR','CV','CW','CX','CY','CZ','DE','DJ','DK','DM','DO','DZ','EC','EE','EG','ER','ES','ET','FI','FJ','FM','FR','GA','GB','GD','GE','GG','GH','GM','GN','GQ','GR','GS','GT','GU','GW','GY','HM','HN','HR','HT','HU','ID','IE','IL','IN','IQ','IS','IT','JE','JM','JO','JP','KE','KG','KH','KI','KM','KN','KR','KW','KZ','LA','LB','LC','LI','LK','LR','LS','LT','LU','LV','LY','MA','MC','MD','ME','MG','MH','MK','ML','MM','MN','MP','MR','MT','MU','MV','MW','MX','MY','MZ','NA','NC','NE','NF','NG','NI','NL','NO','NP','NR','NU','NZ','OM','PA','PE','PF','PG','PH','PK','PL','PM','PN','PT','PW','PY','QA','RO','RS','RU','RW','SA','SB','SC','SE','SG','SH','SI','SK','SL','SM','SN','SO','SR','ST','SV','SX','SZ','TD','TF','TG','TH','TJ','TK','TL','TM','TN','TO','TR','TT','TV','TZ','UA','UG','UM','US','UY','UZ','VA','VC','VE','VN','VU','WF','WS','YE','ZA','ZM','ZW']
countries = { 
	'AD':'Andorra',
        'AE':'United Arab Emirates',
	'AF':'Afghanistan',
   	'AG':'Antigua and Barbuda',
   	'AL':'Albania',
   	'AM':'Armenia',
   	'AO':'Angola',
   	'AQ':'Antarctica',
   	'AR':'Argentina',
   	'AS':'American Samoa',
   	'AT':'Austria',
   	'AU':'Australia',
   	'AZ':'Azerbaijan',
   	'BA':'Bosnia and Herzegovina',
   	'BB':'Barbados',
   	'BD':'Bangladesh',
   	'BE':'Belgium',
   	'BF':'Burkina Faso',
   	'BG':'Bulgaria',
   	'BH':'Bahrain',
   	'BI':'Burundi',
   	'BJ':'Benin',
   	'BN':'Brunei',
   	'BO':'Bolivia',
	'BQ':'Caribbean Netherlands',
	'BR':'Brazil',
	'BS':'The Bahamas',
	'BT':'Bhutan',
	'BW':'Botswana',
	'BY':'Belarus',
	'BZ':'Belize',
	'CA':'Canada',
	'CC':'Cocos (Keeling) Islands',
	'CD':'Democratic Republic of the Congo',
	'CF':'Central African Republic',
	'CG':'Republic of the Congo',
	'CH':'Switzerland',
	'CI':'Cote d\'Ivoire',
	'CK':'Cook Islands',
	'CL':'Chile',
	'CM':'Cameroon',
	'CN':'China',
	'CO':'Colombia',
	'CR':'Costa Rica',
	'CV':'Cape Verde',
	'CW':'Curacao',
	'CX':'Christmas Island',
	'CY':'Cyprus',
	'CZ':'Czechia',
	'DE':'Germany',
	'DJ':'Djibouti',
	'DK':'Denmark',
	'DM':'Dominica',
	'DO':'Dominican Republic',
	'DZ':'Algeria',
	'EC':'Ecuador',
	'EE':'Estonia',
	'EG':'Egypt',
	'ER':'Eritrea',
	'ES':'Spain',
	'ET':'Ethiopia',
	'FI':'Finland',
	'FJ':'Fiji',
	'FM':'Federated States of Micronesia',
	'FR':'France',
	'GA':'Gabon',
	'GB':'United Kingdom',
	'GD':'Grenada',
	'GE':'Georgia',
	'GG':'Guernsey',
	'GH':'Ghana',
	'GM':'The Gambia',
	'GN':'Guinea',
	'GQ':'Equatorial Guinea',
	'GR':'Greece',
	'GS':'South Georgia and the South Sandwich Islands',
	'GT':'Guatemala',
	'GU':'Guam',
	'GW':'Guinea-Bissau',
	'GY':'Guyana',
	'HM':'Heard Island and McDonald Islands',
	'HN':'Honduras',
	'HR':'Croatia',
	'HT':'Haiti',
	'HU':'Hungary',
	'ID':'Indonesia',
	'IE':'Ireland',
	'IL':'Israel',
	'IN':'India',
	'IQ':'Iraq',
	'IS':'Iceland',
	'IT':'Italy',
	'JE':'Jersey',
	'JM':'Jamaica',
	'JO':'Jordan',
	'JP':'Japan',
	'KE':'Kenya',
	'KG':'Kyrgyzstan',
	'KH':'Cambodia',
	'KI':'Kiribati',
	'KM':'Comoros',
	'KN':'Saint Kitts and Nevis',
	'KR':'South Korea',
	'KW':'Kuwait',
	'KZ':'Kazakhstan',
	'LA':'Laos',
	'LB':'Lebanon',
	'LC':'Saint Lucia',
	'LI':'Liechtenstein',
	'LK':'Sri Lanka',
	'LR':'Liberia',
	'LS':'Lesotho',
	'LT':'Lithuania',
	'LU':'Luxembourg',
	'LV':'Latvia',
	'LY':'Libya',
	'MA':'Morocco',
	'MC':'Monaco',
	'MD':'Moldova',
	'ME':'Montenegro',
	'MG':'Madagascar',
	'MH':'Marshall Islands',
	'MK':'Macedonia (FYROM)',
	'ML':'Mali',
	'MM':'Myanmar (Burma)',
	'MN':'Mongolia',
	'MP':'Northern Mariana Islands',
	'MR':'Mauritania',
	'MT':'Malta',
	'MU':'Mauritius',
	'MV':'Maldives',
	'MW':'Malawi',
	'MX':'Mexico',
	'MY':'Malaysia',
	'MZ':'Mozambique',
	'NA':'Namibia',
	'NC':'New Caledonia',
	'NE':'Niger',
	'NF':'Norfolk Island',
	'NG':'Nigeria',
	'NI':'Nicaragua',
	'NL':'Netherlands',
	'NO':'Norway',
	'NP':'Nepal',
	'NR':'Nauru',
	'NU':'Niue',
	'NZ':'New Zealand',
	'OM':'Oman',
	'PA':'Panama',
	'PE':'Peru',
	'PF':'French Polynesia',
	'PG':'Papua New Guinea',
	'PH':'Philippines',
	'PK':'Pakistan',
	'PL':'Poland',
	'PM':'Saint Pierre and Miquelon',
	'PN':'Pitcairn Islands',
	'PT':'Portugal',
	'PW':'Palau',
	'PY':'Paraguay',
	'QA':'Qatar',
	'RO':'Romania',
	'RS':'Serbia',
	'RU':'Russia',
	'RW':'Rwanda',
	'SA':'Saudi Arabia',
	'SB':'Solomon Islands',
	'SC':'Seychelles',
	'SE':'Sweden',
	'SG':'Singapore',
	'SH':'Saint Helena, Ascension and Tristan da Cunha',
	'SI':'Slovenia',
	'SK':'Slovakia',
	'SL':'Sierra Leone',
	'SM':'San Marino',
	'SN':'Senegal',
	'SO':'Somalia',
	'SR':'Suriname',
	'ST':'Sao Tome and Principe',
	'SV':'El Salvador',
	'SX':'Sint Maarten',
	'SZ':'Swaziland',
	'TD':'Chad',
	'TF':'French Southern and Antarctic Lands',
	'TG':'Togo',
	'TH':'Thailand',
	'TJ':'Tajikistan',
	'TK':'Tokelau',
	'TL':'Timor-Leste',
	'TM':'Turkmenistan',
	'TN':'Tunisia',
	'TO':'Tonga',
	'TR':'Turkey',
	'TT':'Trinidad and Tobago',
	'TV':'Tuvalu',
	'TZ':'Tanzania',
	'UA':'Ukraine',
	'UG':'Uganda',
	'UM':'United States Minor Outlying Islands',
	'US':'United States',
	'UY':'Uruguay',
	'UZ':'Uzbekistan',
	'VA':'Vatican City',
	'VC':'Saint Vincent and the Grenadines',
	'VE':'Venezuela',
	'VN':'Vietnam',
	'VU':'Vanuatu',
	'WF':'Wallis and Futuna',
	'WS':'Samoa',
	'YE':'Yemen',
	'ZA':'South Africa',
	'ZM':'Zambia',
	'ZW':'Zimbabwe',

}
def prompt_for_options():
	
	while True:
		try:
			choose_way = int(raw_input("Enter 1 for Express Settings or Enter 2 to Create Your Own Setup : "))
		except ValueError:
			print("Input a NUMBER Lad")
			continue
		if (choose_way > 2 or choose_way < 1):
			print("Your Choice is not an Option")
			continue
		else:
			break
			
	if choose_way == 1:
		print("You Have Chosen Express Settings")
	elif choose_way ==2:
		print("You Will Need to Specify Your own Settings")
		
	return choose_way
def express_settings():
	print("Available Search Country Codes are: "),
	print(countrycodes)
	while True:
		chosen_country = raw_input("Choose a Valid Search Country using Country Code: ").upper()
		if (len(chosen_country) != 2):
			print("It Must Be Two Characters Only")
			continue
		elif (chosen_country.upper() in countrycodes) and (len(chosen_country) == 2):
			print("You Have Chosen Search Country as: ")
			print(countries[chosen_country])
			break
		else:
			print("You have not Chosen a Searchable Country")
			continue
	while True:
		choose_keyword = raw_input("Enter Keyword or Sentence to Search: ")
		chosen_keyword = str(choose_keyword)
		if (len(chosen_keyword) > 0):
			print("You Have Chosen to Search: ")
			print(chosen_keyword)
			break
		else:
			print("You have not input anything")
			continue
		google_search_url_default = 'https://www.google.' + chosen_country.lower() + '/search?hl=en'
		use_own_ip_default = True
		continue_last_scrape_default = False
		sel_browser_default = 'chrome'
		manual_captcha_solving_default = 'False'
		scrape_method_default = 'selenium'
		search_engines_default = ['google']
		print_results_default = 'summarize'
		num_results_per_page_default = 10
		num_workers_default = 1
		num_pages_for_keyword_default = 5
		maximum_workers_default = 5
		google_sleeping_ranges_default = {
			1:(50,70),
			5:(70,100),
			30:(100,215),
			127:(125,200),
		}
		keywords = [ chosen_keyword ] 
		config = {
			'keywords':keywords,
			'google_search_url':google_search_url_default, 
			'use_own_ip':use_own_ip_default, 
			'continue_last_scrape':continue_last_scrape_default,
			'sel_bowser':sel_browser_default, 
			'manual_captcha_solving':manual_captcha_solving_default,
			'scrape_method':scrape_method_default,
			'search_engines':search_engines_default,
			'print_results':print_results_default,
			'num_results_per_page':num_results_per_page_default,
			'num_workers':num_workers_default,
			'num_pages_for_keyword':num_pages_for_keyword_default,
			'google_sleeping_ranges':google_sleeping_ranges_default,
			'maximum_workers':maximum_workers_default
		}

	return config

def custom_settings():
	
	available_engines = { 
		'1':'Google',
		'2':'Yandex',
		'3':'Bing',
		'4':'Yahoo',
		'5':'Baidu',
		'6':'DuckDuckGo',
		'7':'Ask'
	}
	scrape_method_default = 'selenium'
	print_results_default = 'summarize'
	maximum_workers_default = 20
	google_sleeping_ranges_default = {
		1:(50,70),
		5:(70,100),
		30:(100,215),
		127:(125,200),
	}

	print("Available Search Country Codes are: "),
	print(countrycodes)

	while True:
		chosen_country = raw_input("Choose a Valid Search Country using Country Code: ").upper()
		if (len(chosen_country) != 2):
			print("It Must Be Two Characters Only")
			continue
		elif (chosen_country.upper() in countrycodes) and (len(chosen_country) == 2):
			print("You Have Chosen Search Country as: ")
			print(countries[chosen_country])
			google_search_url_user = 'https://www.google.' + chosen_country.lower() + '/search?hl=en'
			break
		else:
			print("You have not Chosen a Searchable Country")
			continue

	while True:
		choose_keyword = raw_input("Enter Keyword or Sentence to Search: ")
		chosen_keyword = str(choose_keyword)
		if (len(chosen_keyword) > 0):
			print("You Have Chosen to Search: ")
			print(chosen_keyword)
			break
		else:
			print("You have not input anything")
			continue

	while True:
		choose_browser = raw_input("Choose Scrape Browser! Enter 1 to choose Chrome, 2 to choose Firefox, 3 to choose Phantomjs, nothing to choose default: ")
		
		if int(choose_browser) == 1:
			sel_browser_user = 'Chrome'
			print("You Have Chosen Chrome: ")
			break
		elif int(choose_browser) == 2:
			sel_browser_user = 'Firefox'
			print("You Have Chosen Chrome: ")
			break
		elif int(choose_browser) == 3:
			sel_browser_user = 'Phantomjs'
			print("You Have Chosen Phantomjs: ")
			break
		elif choose_browser =='':
			sel_browser_user = 'Chrome'
			print("The default Browser is Chrome")
			break
		else:
			print("Make a Valid Choice")
			continue

	while True:
		search_engines_user = [ ]
		try:
			choose_engines = int(raw_input("Choose Search Engine options, you can enter more than one 1. Google, 2. Yandex, 3. Bing, 4. Yahoo, 5. Baidu, 6. DuckDuckGo, 7. Ask "))
		except ValueError:
			print("Input a valid single number or a series of numbers in any order")
			continue
		choose_engines = str(choose_engines)
						   
		from itertools import permutations				   
		if choose_engines in itertools.permutations('1234567', 1):
			search_engines_user = [available_engines[choose_engines]]
			print("Your Choice was: ", available_engines[choose_engines])
			break
						   
		elif choose_engines in itertools.permutations('1234567', 2):
			for choice in choose_engines:
				search_engines_user = search_engines_user.append(available_engines[choose_engines])
				print("You have Chosen: ", available_engines[choose_engines])
			break
		
		elif choose_engines in itertools.permutations('1234567', 3):
			for choice in choose_engines:
				search_engines_user = search_engines_user.append(available_engines[choose_engines])
				print("You have Chosen: ", available_engines[choose_engines])
			break			   
		
		elif choose_engines in itertools.permutations('1234567', 4):
			for choice in choose_engines:
				search_engines_user = search_engines_user.append(available_engines[choose_engines])
				print("You have Chosen: ", available_engines[choose_engines])
			break			   
		
		elif choose_engines in itertools.permutations('1234567', 5):
			for choice in choose_engines:
				search_engines_user = search_engines_user.append(available_engines[choose_engines])
				print("You have Chosen: ", available_engines[choose_engines])
			break
		
		elif choose_engines in itertools.permutations('1234567', 6):
			for choice in choose_engines:
				search_engines_user = search_engines_user.append(available_engines[choose_engines])
				print("You have Chosen: ", available_engines[choose_engines])
			break				   
		
		elif choose_engines in itertools.permutations('1234567', 7):
			for choice in choose_engines:
				search_engines_user = search_engines_user.append(available_engines[choose_engines])
				print("You have Chosen: ", available_engines[choose_engines])
			break			   
		else:
			continue
						       
	while True:
		continue_last_scrape_user = (raw_input("Do You Want to Continue Last Scrape: Y/N or Enter for default ") or 'N').lower()
		if continue_last_scrape_user == 'n':
			continue_last_scrape_user = False
			print("Last Scrape Will not be Continued")
			break
		elif continue_last_scrape_user == 'y':
			continue_last_scrape_user = True
			print("Last Scrape Will be Continued!")
			break
		else:
			print("Make a Valid Choice")
			continue
	
	while True:
		manual_captcha_solving_user = (raw_input("Do You Want to Solve Captcha Manually, if You select False if there is a captcha the page will not be processed: Y/N or Enter for Default ") or 'N').lower()
		if manual_captcha_solving_user == 'n':
			manual_captcha_solving_user = False
			print("Captcha will not be Solved")
			break
		elif manual_captcha_solving_user == 'y':
			manual_captcha_solving_user = True
			print("Captcha will be Solved by You")
			break
		else:
			print("Make a Valid Choice")
			continue
			
	
	while True:
		use_own_ip_user = (raw_input("Do You Want to use Your own IP for the search, if You select False if there is no proxy specified the search will not be performed: Y/N or Enter for Default ") or 'Y').lower()
		if use_own_ip_user == 'n':
			use_own_ip_user = False
			print("Proxy must be Specified")
			while True:
				print("Proxies must be of one of the following formats 'socks5 23.212.45.13= 1080 username= password' 'socks4 23.212.45.13= 80 username= password' 'http 23.212.45.13= 80'")
				proxy_file_user = raw_input("Specify a Vaild path to a Proxy file")
				break
			break
		elif use_own_ip_user == 'y':
			use_own_ip_user = True
			print("Your IP will be Used")
			break
		else:
			print("Make a Valid Choice")
			continue
	
	while True:
		try:
			num_pages_for_keyword_user = int(raw_input(" Enter How Many Pages of Google Results will be scraped between 1 and 15 or press Enter for Default ") or 5)
		except ValueError:
			print("Must be a Number")
			continue
		if (num_pages_for_keyword_user < 1 and num_pages_for_keyword_user > 15):
			print("Enter a Valid Number")
			continue
		else:
			print("You Have Chosen ", num_pages_for_keyword_user, "pages")
			break
				      
	
	while True:
		try:
			num_results_per_page_user = int(raw_input(" Enter How Many results will be displayed per page between 1 and 15 or press Enter for Default ") or 10)
		except ValueError:
			print("Must be a Number")
			continue
		if (num_results_per_page_user < 1 and num_results_per_page_user > 15):
			print("Enter a Valid Number")
			continue
		else:
			print("You Have Chosen ", num_results_per_page_user, "results per page")
			break
	while True:
		try:
			num_workers_user = int(raw_input(" Enter How Many Browser instances will perform the search 1 and 10 or press Enter for Default ") or 1)
		except ValueError:
			print("Must be a Number")
			continue
		if (num_workers_user < 1 and num_workers_user > 10):
			print("Enter a Valid Number")
			continue
		else:
			print("You Have Chosen ", num_results_per_page_user, "results per page")
			break
	
	keywords = [ chosen_keyword ] 
	config = {
		'keywords':keywords,
		'google_search_url':google_search_url_user, 
		'use_own_ip':use_own_ip_user, 
		'continue_last_scrape':continue_last_scrape_user,
		'sel_bowser':sel_browser_user, 
		'manual_captcha_solving':manual_captcha_solving_user,
		'scrape_method':scrape_method_default,
		'search_engines':search_engines_user,
		'print_results':print_results_default,
		'num_results_per_page':num_results_per_page_user,
		'num_workers':num_workers_user,
		'num_pages_for_keyword':num_pages_for_keyword_user,
		'google_sleeping_ranges':google_sleeping_ranges_default,
		'maximum_workers':maximum_workers_default
	}
	return config
def start_search(config):
	urls_to_process = deque([ ])
	try:
		search = scrape_with_config(config)
	except GoogleSearchError as e:
		print(e)

	for serp in search.serps:
		print(serp)

		for link in serp.links:
			retrieved_url = str(link)
			urls_to_process = urls_to_process.append(retrieved_url)
	return urls_to_process

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
def rainmail():
	if prompt_for_options() == 1:
		print(process_urls(start_search(express_settings())))
	elif prompt_for_options() == 2:
		print(process_urls(start_search(custom_settings())))
	return True
rainmail()
		
	
