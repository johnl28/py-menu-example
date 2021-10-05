
# close func
def CloseFunc():
	print("CloseFunc")
	return False

# an option
def Option1():
	print("Option1")
	return True

# dictionary with all options_dict
# your key : ("option name", function to call for that option),
options_dict = {
	0 : ("Close called", CloseFunc),
	1 : ("Option1 function called", Option1),	
}

# ask for option function
def AskForOption():
	#print each option you have with the coresponded key
	for key in options_dict.keys():
		print("%s - %s" % (str(key), options_dict[key][0])) 
	print("")
	
	
	option = input("Enter your option:") # ask for the option
	if not option in options_dict: # check if the key exists in your option dict
		print("Invalid input")
		return True
	
	return options_dict[option][1]() # call the function by the key entered and return the value

if __name__ == "__main__":
	# ask for an option until AskForOption will be false
	while AskForOption():
		pass





