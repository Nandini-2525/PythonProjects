# accept 2 no and 1 operator from user
# and corresponding operator performs operation

a= int(input("Enter number"))
opr = input("Enter any operator")
b= int(input("Enter number"))


if opr=='+':
    print(a+b)
elif opr=='-':
    print(a-b)
elif opr=='*':
    print(a*b)
elif opr=='/':
    print(a/b)
elif opr=='%':
    print(a%b)
else:
    print("Please enter a valid character")
