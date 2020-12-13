i=int(input("Please enter the integer-->"))
print('All the prime numbers till',i, 'are-')
for n in range(2,i):
    for x in range(2,n):
        if n%x==0:
            break
    else:
        print(n,)
input("Press enter to exit")
            