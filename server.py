fobj = open("operations1.txt","r")
opr_list = fobj.readlines()
fobj.close()

i = 0
while i<len(opr_list):
    a = opr_list[i].split(",")
    if len(a) == 3:
        ans = str(eval(a[0]+a[1]+a[2]))
        res_string = a[0] + a[1] + a[2][:len(a[2])-1] + "=" + ans + "\n"
        opr_list[i] = res_string
    i = i + 1

fobj = open("operations1.txt", "w")
fobj.writelines(opr_list)
fobj.close()
print("Response Sent...")

