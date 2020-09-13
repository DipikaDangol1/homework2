
lst=[]
s=input("enter a string: ")
l = list(s)
n=len(s)
ns=""
for i in range(0,n):
	indices=int(input("enter indices:"))
	lst.append(indices)
for i in lst:
	ns=ns+s[i]
print (ns)
