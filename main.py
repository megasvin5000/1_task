def fib(n):
	a = [0, 1]
	print(0)
	print(1)
	for i in range(2, n):
		z = a[i-1] + a[i-2]
		a.append(z)
		print(z)


print('Hello, World!')
