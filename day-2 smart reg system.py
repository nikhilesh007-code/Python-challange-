a=input("Enter student ID:")
b=input("Enter Email ID:")
c=input("Enter password:")
d=input("Enter referral code:")
e=1
if len(a)!=7:
    e=0
else:
    if a[0:3]!="CSE":#stuid check
        e=0
    if a[3]!="-":
        e=0
    if a[4].isdigit()==False or a[5].isdigit()==False or a[6].isdigit()==False:
        e=0
if b.count("@")<1 or b.count(".")<1:#email check
    e=0
if b[0]=="@" or b[len(b)-1]=="@":
    e=0
if b[-4:]!=".edu":
    e=0
if(len(c))<8:#pass check
    e=0
f=0
if c[0].isdigit():
    f=1
if c[1].isdigit():
    f=1
if c[2].isdigit():
    f=1
if c[3].isdigit():
    f=1
if c[4].isdigit():
    f=1
if c[5].isdigit():
    f=1
if c[6].isdigit():
    f=1
if c[7].isdigit():
    f=1
if f==0:
    e=0
if c[0].isupper()==False:
    e=0
if d[0:3]!="REF":#ref check
    e=0
if d[5]!="@":
    e=0
if len(d)!=6:
    e=0
if d[3].isdigit()==False or d[4].isdigit()==False:
    e=0
if e==1:
    print("APPROVED")
else:

    print("REJECTED")
