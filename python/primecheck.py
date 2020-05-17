def is_prime(number):
	prime = True
	divisor = 1
	for x in range(2, number // 2):
		if number % x == 0:
			prime = False
			divisor = x
			break
	if prime:
		print("the number is a prime")
		return True
	else:
		print("the number is divisible by",divisor)
		return False
a = int (input())
is_prime(a)

