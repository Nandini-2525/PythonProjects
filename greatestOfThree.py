# to print gratest of 3 num
a,b,c= [int(x) for x in input("Enter values").split(",")]
if a>b and a>c:print(f"{a} is greater")
elif b>a and b>c:ptint(f"{b} is greater")
elif c>a and c>b:print(f"{c} is grater")
else:print("Enter valid number")
