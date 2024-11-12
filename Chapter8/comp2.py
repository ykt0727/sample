print([x * x for x in range(10)])

print({x * x for x in range(10)})

print({x * x : x for x in range(10)})

print([x for x in range(20) if x % 2 and x % 3])

print(['Fizz' if x % 3 == 0 else x for x in range(1, 16)])