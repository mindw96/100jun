N = int(input())
sol = N

for i in range(len(str(N)) - 1, -1, -1):
#    print(N // (10 ** i))
    sol += N // (10 ** i)
    N -= (N // (10 ** i)) * (10 ** i)
#    print(N)
    print(sol, N // (10 ** i))
print(sol, N)
print('Test')
