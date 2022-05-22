a=float(input("Enter the first number "))
b=float(input("Enter the second number "))
c=float(input("Enter the third number "))
if a>b:
    if b>c:
        print(a,"is the greatest of all.")
elif b>a:
    if b>c:
        print(b,"is the greatest of all.")    
else:
    print(c,"is the greatest of all.")  



