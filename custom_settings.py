#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#function to set user defined search parameters

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
	sleeping_ranges_default = {
		1:  (1, 2),
		5:  (2, 4),
		30: (10, 20),
		127: (30, 50),
	}
	google_sleeping_ranges_default = {
		1:  (2, 3),
		5:  (3, 5),
		30: (10, 20),
		127: (30, 50),
	}

	print("Available Search Country Codes are: "),
	print(countrycodes)

	while True:
		chosen_country = str(input("Choose a Valid Search Country using Country Code: ")).upper()
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
		choose_keyword = input("Enter Keyword or Sentence to Search: ")
		chosen_keyword = str(choose_keyword)
		if (len(chosen_keyword) > 0):
			print("You Have Chosen to Search: ")
			print(chosen_keyword)
			break
		else:
			print("You have not input anything")
			continue

	while True:
		try:
			choose_browser = int(input("Choose Scrape Browser! Enter 1 to choose Chrome, 2 to choose Firefox, 3 to choose Phantomjs Press Enter to Choose Default: " ) or 1)
		except ValueError:
			print("Choose a Valid Input or Press Enter to Choose Default")
			continue
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
		else:
			print("Make a Valid Choice")
			continue

	while True:
		search_engines_use = []
		search_engines_user = []
		try:
			choose_engines = int(input("Choose Search Engine options, you can enter more than one 1. Google, 2. Yandex, 3. Bing, 4. Yahoo, 5. Baidu, 6. DuckDuckGo, 7. Ask "))
		except ValueError:
			print("Input a valid single number or a series of numbers in any order")
			continue
		choose_engines = str(choose_engines)
				   
		if choose_engines in [''.join(i) for i in permutations('1234567', 1)]:
			search_engines_user = [available_engines[choose_engines]]
			print("Your Choice was: ", available_engines[choose_engines])
			break
						   
		elif choose_engines in [''.join(i) for i in permutations('1234567', 2)]:
			for choice in choose_engines:
				search_engines_user.append(available_engines[str(choice)])
				print("You have Chosen: ", available_engines[str(choice)])
			break
		
		elif choose_engines in [''.join(i) for i in permutations('1234567', 3)]:
			for choice in choose_engines:
				search_engines_user.append(available_engines[str(choice)])
				print("You have Chosen: ", available_engines[str(choice)])
			break			   
		
		elif choose_engines in [''.join(i) for i in permutations('1234567', 4)]:
			for choice in choose_engines:
				search_engines_user.append(available_engines[str(choice)])
				print("You have Chosen: ", available_engines[str(choice)])
			break			   
		
		elif choose_engines in [''.join(i) for i in permutations('1234567', 5)]:
			for choice in choose_engines:
				search_engines_user.append(available_engines[str(choice)])
				print("You have Chosen: ", available_engines[str(choice)])
			break
		
		elif choose_engines in [''.join(i) for i in permutations('1234567', 6)]:
			for choice in choose_engines:
				search_engines_user.append(available_engines[str(choice)])
				print("You have Chosen: ", available_engines[str(choice)])
			break				   
		
		elif choose_engines in [''.join(i) for i in permutations('1234567', 7)]:
			for choice in choose_engines:
				search_engines_user.append(available_engines[str(choice)])
				print("You have Chosen: ", available_engines[str(choice)])
			break			   
		else:
			continue
				
	print(search_engines_user)		       
	while True:
		continue_last_scrape_user = str(input("Do You Want to Continue Last Scrape: Y/N or Enter for default ") or 'N').lower()
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
		manual_captcha_solving_user = str(input("Do You Want to Solve Captcha Manually, if You select False if there is a captcha the page will not be processed: Y/N or Enter for Default ") or 'N').lower()
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
		use_own_ip_user = str(input("Do You Want to use Your own IP for the search, if You select False if there is no proxy specified the search will not be performed: Y/N or Enter for Default ") or 'Y').lower()
		if use_own_ip_user == 'n':
			use_own_ip_user = False
			print("Proxy must be Specified")
			while True:
				print("Proxies must be of one of the following formats 'socks5 23.212.45.13= 1080 username= password' 'socks4 23.212.45.13= 80 username= password' 'http 23.212.45.13= 80'")
				proxy_file_user = input("Specify a Vaild path to a Proxy file")
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
			num_pages_for_keyword_user = int(input(" Enter How Many Pages of Google Results will be scraped between 1 and 50 or press Enter for Default ") or 10)
		except ValueError:
			print("Must be a Number")
			continue
		if (num_pages_for_keyword_user < 1 and num_pages_for_keyword_user > 150):
			print("Enter a Valid Number")
			continue
		else:
			print("You Have Chosen ", num_pages_for_keyword_user, "pages")
			break
				      
	
	while True:
		try:
			num_results_per_page_user = int(input(" Enter How Many results will be displayed per page between 1 and 15 or press Enter for Default ") or 10)
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
			num_workers_user = int(input(" Enter How Many Browser instances will perform the search 1 and 10 or press Enter for Default ") or 1)
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
		'maximum_workers':maximum_workers_default,
		'search_offset':1,
		'sleeping_ranges':sleeping_ranges_default,
		'google_sleeping_ranges':google_sleeping_ranges_default,

	}
	return config

     
    
