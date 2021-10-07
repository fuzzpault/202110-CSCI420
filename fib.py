
memory = {}

def fib(n, depth = 0):
	d = "   " * depth
	if n in memory.keys():
		print(f"{d}{n} from cache")
		return memory[n]
	
	if n <= 2:
		memory[n] = 1
		return 1
	print(f"{d} computing f({n})")
	ret = fib(n-1, depth +1) + fib(n-2, depth + 1)
	memory[n] = ret
	return ret

fib(6)

fib(56)