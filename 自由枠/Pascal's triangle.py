from copy import deepcopy
N = int(input())
A = []
B = []
for i in range(1, N+1):
    B = deepcopy(A)
    A = []
    if i == 1:
        print(1,end=' ')
    elif i == 2:
        print(1, 1,end=' ')
        A = [1, 1]
    else:
        for ii in range(1, i+1):
            if ii == 1 or ii == i:
                A.append(1)
                print(1,end=' ')
            else:
                A.append(B[ii-2] + B[ii-1])
                print(B[ii-2] + B[ii-1],end=' ')
    print() 