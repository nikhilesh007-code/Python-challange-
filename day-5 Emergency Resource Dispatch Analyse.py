resreq=[]#list of resourse req and input from user
n=int(input("enter activity no of resource requests:"))
for i in range(n):
    m = int(input(f"Enter the element {i+1} in list:"))
    resreq=resreq+[m]
#empty lists to store vals based on cat
low=[]
moderate=[]
high=[]
invalid=[]
valid=0
ignored=0
removed=0
for j in resreq:
    if j<0:
        invalid=invalid+[j]
        ignored+=1
    elif j==0:
        valid+=1
    elif j>=1 and j<=20:
        low=low+[j]
        valid+=1
    elif j>=21 and j<=50:
        moderate=moderate+[j]
        valid+=1
    else:
        high=high+[j]
        valid+=1
print("low demand:",low)
print("moderate demand:",moderate)
print("high demand:",high)
print("invalid requests:",invalid)
print("valid requests:",valid)
print("ignored requests:",ignored)
#personalisation based on lucky no enter by user
luck=int(input("enter your lucky number:"))
perlog=luck%3
if perlog==0:
    removed=len(low)
    low=[]
elif perlog==1:
    removed=len(high)
    high=[]
else:
    removed=len(low)+len(high)
    low=[]
    high=[]
print("after personalization:")
print("low demand:",low)
print("moderate demand:",moderate)
print("high demand:",high)
print("invalid requests:",invalid)
print("valid requests:",valid)
print("ignored requests:",ignored)
print(f"your lucky number is {luck}")
print(f"your personalisation logic number is {perlog}")
print("removed requests:",removed)



