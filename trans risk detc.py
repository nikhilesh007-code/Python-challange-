trans=[]
n=int(input("Enter no of transactions:"))
for i in range(n):
    m=int(input(f"Enter transaction {i+1}: "))
    trans=trans+[m]
cat={
    "normal":[],
    "large":[],
    "highrisk":[],
    "invalid":[]
}
for i in trans:
    if i<=0:
        cat["invalid"]=cat["invalid"]+[i]
    elif i>=1 and i<=500:
        cat["normal"]=cat["normal"]+[i]
    elif i>=501 and i<=2000:
        cat["large"]=cat["large"]+[i]
    else:
        cat["highrisk"]=cat["highrisk"]+[i]
validtrans=[i for i in trans if i>0]
totvalue=0
for j in validtrans:
    totvalue+=j
notrans=len(trans)
if(notrans>5):
    freq="Yes"
else:
    freq="No"
if(totvalue>5000):
    largespend="Yes"
else:
    largespend="No"
if(len(cat["highrisk"])>=3):
    suspicious="Yes"
else:
    suspicious="No"
if suspicious=="Yes"or(largespend=="Yes" and freq=="Yes"):
    risk="High Risk"
elif largespend=="Yes" or freq=="Yes":
    risk="Moderate Risk"
else:
    risk="Low Risk"
summary=("total transaction:",totvalue,"no of transaction:",notrans,"risk level:",risk)
print("Transactions:")
print("Normal:",cat["normal"])
print("Large:",cat["large"])
print("High Risk:",cat["highrisk"])
print("Invalid:",cat["invalid"])
print("Total Transaction Value:",totvalue)
print("Number of transactions:",notrans)
print("Frequent Transactions:",freq)
print("Large Spending Transactions:",largespend)
print("Suspicious Transactions:",suspicious)
print("Risk Level of Transactions:",risk)
print("Summary:")
print(summary[0],summary[1])
print(summary[2],summary[3])
print(summary[4],summary[5])