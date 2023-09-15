# admission eligibility

m= int(input("Enter marks:")) 
p= int(input("Enter marks:")) 
c = int(input("Enter marks:")) 
tot =m+p+c
print(tot)

if m>=65 and p>=55 and c>=50 and tot>=150:
    print("Student is eligible")
else:
    print("Student is not eligible")
