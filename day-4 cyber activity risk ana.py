ascores=[]#list of act scores and input from user
n=int(input("enter activity no of activity scores:"))
for i in range(n):
    m = int(input(f"Enter the element {i+1} in list:"))
    ascores=ascores+[m]
#reg no extract
reg_no=int(input("enter the registration number:"))
D=reg_no%10
print(f"D value is {D}")
#empty lists to store vals based on cat
low=[]
med=[]
high=[]
critical=[]
removed=0
valid=0
ignored=0
for j in ascores:
    if j<0:
        ignored+=1
    else:
        valid+=1
        if j>100:
            critical=critical+[j]
        elif j>=61:
            high=high+[j]
        elif j>=31:
            med=med+[j]
        else:
            low=low+[j]
print("low risk:",low)
print("medium risk:",med)
print("high risk:",high)
print("critical risk:",critical)
if(D%2==0):
    removed=len(low)
    low=[]
else:
    removed=len(critical)
    critical=[]
print("After Personalized Filtering:")
print("low risk:",low)
print("medium risk:",med)
print("high risk:",high)
print("critical risk:",critical)
print("Total Valid Entries:",valid)
print("Total Ignored Entries:",ignored)
print("Total Removed Entries:",removed)

