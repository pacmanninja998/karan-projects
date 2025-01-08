def collatz(n):
	count = 0
	while (n != 1):
		if n % 2 == 0:
			n = n / 2
			count += 1
		else:
			n = (n * 3) + 1
			count += 1
	return count

# Test the first 100 numbers
for i in range(1, 101):
	print("Number: " + str(i) + "\tSteps to 1: " + str(collatz(i)))
