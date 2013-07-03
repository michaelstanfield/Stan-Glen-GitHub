def ATM(amount):

	# ATM machine change given in $50s and $20s
	initalAmount = amount
	n50s = 0;
	n20s = 0;
	finish = False;
	
	while finish == False:
		if amount % 50 == 0:
			n50s = amount / 50;
			finish = True;
		else:
			amount = amount - 20;
			n20s = n20s + 1;
	print ("you have withdrawn " + str(amount+(n20s*20)));
	print ("you will receive " + str(n50s) + " $50 notes and " + str(n20s) + " $20 notes");
