#!/usr/bin/env python3
# -*- coding: utf-8 -*-
	
#function to set default search parameters

def express_settings():
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
			break
		else:
			print("You have not Chosen a Searchable Country")
			continue
	while True:
		choose_keyword = str(input("Enter Keyword or Sentence to Search: "))
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
	num_pages_for_keyword_default = 20
	maximum_workers_default = 20
	keywords = [ chosen_keyword ] 
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
		'maximum_workers':maximum_workers_default,
		'search_offset':1,
		'sleeping_ranges':sleeping_ranges_default,
		'google_sleeping_ranges':google_sleeping_ranges_default

		}

	return config

     
    

     




