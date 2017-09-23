#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def custom_settings():
	use_own_ip_default = True
	continue_last_scrape_default = False
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
		try:
			choose_way = int(raw_input("Choose Search Engine options, you can enter more than one 1. Google, 2. Yandex, 3. Bing, 4. Yahoo, 5. Baidu, 6. DuckDuckGo, 7. Ask ))
		except ValueError:
			print("Input a single number or a series of numbers")
			continue
		if (choose_way > 2 or choose_way < 1):
			print("Your Choice is not an Option")
			continue
		else:
			break

		
		keywords = [ chosen_keyword ] 
		config = {
			'google_search_url':google_search_url_user, 
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
		}

     
    

     



'''

# See in the config.cfg file for possible values
config = {
    'use_own_ip': True,
    'keywords': keywords,
    'search_engines': ['google'],   #add other search engines if you need
    'num_pages_for_keyword': 50,
    'scrape_method': 'selenium',
    'sel_browser': 'chrome',
}

try:
	search = scrape_with_config(config)
except GoogleSearchError as e:
	print(e)'''

'''f = open('searchresultlinks.txt','w')    #indicate name of output file with google search links
sys.stdout = f
path= '/home/Desktop'

for serp in search.serps:
	#print(serp)

	for link in serp.links:
		#print(link)
		print (link, f)  # or f.write('...\n')  print each link to the file
f.close()'''
