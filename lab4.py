num = int(input("Enter a number: "))
st = int(input("Enter a limit: "))
f = 1
while f <= num:
    first = 1
    while first <= st:
        ans = f * first
        print(ans,end=" " )
        # first += 1
        first += 1
    print()
    f += 1
