# Find N Numbers Sum And Average

n=int(input('Enter the number-'))
s=0
for i in range(n):
    a=int(input('Enter the values-'))
    s=s+a

print(f' sum of Numbers is {s}')
    
print(f'Average of Numbers is {s/n}')
