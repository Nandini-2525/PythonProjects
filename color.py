# accept any char from user and print corresponding color name

clr = input("Enter the color character:")
if clr=='p' or clr=='P':
    print("Pink")
elif clr=='r' or clr=='R':
    print("Red")
elif clr=='y' or clr=="y":
    print("Yellow")
else:
    print("Enter valid character")
