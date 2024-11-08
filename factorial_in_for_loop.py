n=7
fact=1
if n==0:
    print("factorial")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("The factorial of",n,"is",fact )