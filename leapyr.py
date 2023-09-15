#wap to check given year is leap or not
# year%4==0 OR year %400 but not year%100

yr = int(input("Enter the year: "))

if(yr%4==0 or yr%400==0 and yr%100!=0):
    print(f"{yr} is leap year")
else:
    print(f"{yr} is not leap year")
