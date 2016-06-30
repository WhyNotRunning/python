# -.- charting = utf-8 -.-
def accumulate():
	tally = 0
	while 1:
		next = yield
		if next is None:
			return tally
		tally += next

def gather_tallies(tallies):
	while 1:
	 	tally = yield from accumulate()
	 	tallies.append(tally)

if __name__=='__main__':
 	tallies = [1,2]
 	acc = gather_tallies(tallies)
 	next(acc)# Ensure the accumulator is ready to accept values
 	acc.send(1)
 	acc.send(1)
 	acc.send(None) # Finish the first tally
 	for x in range(4):
 		acc.send(x)
 	acc.send(5)
 	acc.send(None) # Finish the second tally
 	print(tallies)