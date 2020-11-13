
def find_cheapest(weight):
	if weight <= 2:
		if(20+1.5*weight < 4.5*weight):
			return 20+1.5*weight
		else:
			return 4.5*weight
	elif weight > 2 and weight <=6:
		if(20+3.0*weight<9.0*weight):
			return 20+3.0*weight
		else:
			return 9.0*weight
	elif weight > 6 and weight <= 10:
		if(20+4.0*weight<12*weight):
			return 20+4.0*weight
		else:
			return 12*weight
	else:
		if(20+4.75*weight<14.25*weight):
			return 20+4.75*weight
		else:
			return 14.25*weight

print(find_cheapest(5.3))