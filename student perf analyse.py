n=int(input("enter the number of students:"))
slist=[0]*n#preinitialize all to zero of n size list
slist1=[0]*n
val=0
fail=0
valusr=0
for i in range(n):
    slist[i]=int(input(f"enter student {i+1} marks: "))
    slist1[i]=input(f"enter student {i+1} leetcode username: ")
for i in range(n):
    if(len(slist1[i])>=6):#if leetcode username length>=6 it is valid
        valusr+=1
for i in range(n):
    if(slist[i]>=90 and slist[i]<=100):
        print(slist[i],"-> Excellent")
        val+=1
    elif(slist[i]>=75 and slist[i]<90):
        print(slist[i],"-> Very Good")
        val+=1
    elif(slist[i]>=60 and slist[i]<75):
        print(slist[i],"-> Good")
        val+=1
    elif(slist[i]>=40 and slist[i]<60):
        print(slist[i],"-> Average")
        val+=1
    elif(slist[i]>=0 and slist[i]<40):
        print(slist[i],"-> Fail")
        val+=1
        fail+=1
    else:
        print(slist[i],"->Invalid")
print("Total Valid Students:",val)
print("Total Failed Students:",fail)
print("Total Valid LeetCode Username:",valusr)






