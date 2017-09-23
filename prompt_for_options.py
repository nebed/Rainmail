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
       
