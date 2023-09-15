#show calculations except 45*3=55, 56+9=77, 56/6=4

a= int(input("Enter first number: "))
opr = input("Enter any operator: ")
b= int(input("Enter second number: "))


if a==45 and opr=='*' and b==3:
    print("555")
elif a==56 and opr=='+' and b==9:
    print("77")
elif a==56 and opr=='/' and b==6:
    print("4")
else:
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
