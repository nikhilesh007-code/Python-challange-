a=input("Enter your full name:")
b=input("Enter your email id:")
c=input("Enter your mobile number:")
d=int(input("Enter Age:"))
e=1
if a[0]==' ' or a[len(a)-1]==' ' or a.count(' ')<1:#name validation
    e=0
x=b.count('@')
y=b.count('.')
if x<1 or y<1 or a[0]=='@':#email validation
   e=0
if len(c)!=10 or c[0]=='0' or c.isdigit()==False:#ph validation
   e=0
if d<18 or d>60:#age validation
   e=0
if e==1:
    print("User Profile is Valid")
else:
    print("User Profile is Invalid")
