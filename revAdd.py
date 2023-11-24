n=int(input("Enter a number:"))
r=0
sum=0
while n>0:
  a=n%10
  r=r*10+a
  sum= sum +a
  n=n//10
print(r)
print(sum)
