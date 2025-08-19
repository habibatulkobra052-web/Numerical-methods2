a=float(input("1st:"))
b=float(input("2nd:"))
op=input("OP(+,-,*,/):")
if op=="+":print(a+b)
elif op=="-":print(a-b)
elif op=="*":print(a*b)
elif op=="/":print(a/b)
else:
    print("Invalid operator")