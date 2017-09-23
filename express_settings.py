#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
		}

     
    

     




