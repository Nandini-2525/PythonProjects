opr_ls = ["abc", "+", "-", "*", "/", "%", "<", ">", "**"]


while True:
    print("1 -> Addition")
    print("2 -> Subtraction")
    print("3 -> Multiplication")
    print("4 -> Division")
    print("5 -> Remainder")
    print("6 -> Smaller")
    print("7 -> Greater")
    print("8 -> Power")
    print("9 -> exit")


    ch = int(input("Provide Your Choice:"))

    if ch!=9:
        operation = opr_ls[ch]
        num1 = input("Enter First number")
        num2 = input("Enter Second Number")

        fobj = open("operations1.txt","a")
        fobj.writelines(num1 + "," + operation + "," + num2 + "\n")
        fobj.close()

        print("Request posted successfully....")
        input()

    else:
        exit(0)
