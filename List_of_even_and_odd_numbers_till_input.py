even_numbers=[]
odd_numbers=[]

i=int(input('Please enter any Number->'))

for i in range(1,i+1):
    if i%2==0:
        even_numbers.append(i)
        continue
    odd_numbers.append(i)

print('The set of all even numbers till',i,'is->')
print(even_numbers)

print('The set of all odd numbers till',i,'is->')
print(odd_numbers)