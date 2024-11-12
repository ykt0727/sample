A = 0
for i in range(5):
    try:
        a = int(input())
        A += a
    except ValueError:
        print('error')
print(A)