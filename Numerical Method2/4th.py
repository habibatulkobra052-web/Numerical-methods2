n=int(input("Enter a number:"))
prime_number=True
if n<=1:
    prime_number=False
else:
    for i in range(2,n):
        if n%i==0:
            prime_number=False
            break
        if prime_number:
            print("Prime")
        else:
            print("Not prime")