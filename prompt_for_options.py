def prompt_for_options():
	
	while True:
		try:
			choose_way = int( input("Enter 1 for Express Settings or Enter 2 to Create Your Own Setup : "))
		except ValueError:
			print("Input a NUMBER Lad")
			continue
		if choose_way == 1:
			print("You Have Chosen Express Settings")
			break
		elif choose_way ==2:
			print("You Will Need to Specify Your own Settings")
			break
		
		else:
			print("Make a Valid Choice")
			continue
	return choose_way
       
