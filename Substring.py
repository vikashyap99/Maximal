def max_length(li,maxx):
	xx=0
	for i in range(26):
		if(li[i]):
			xx+=1
	return (xx==maxx)


s = input() 
n = len(s)
ls = [0]*40
for i in range(n):
	ls[ord(s[i])-ord('a')]=1
maxx=0
ans = 1
for i in range(26):
	maxx += ls[i]
low=1
high=n
while(low<=high):
	mid=(low+high)//2
	f=[0]*30
	x=0
	for i in range(mid):
		f[ord(s[i])-ord('a')] += 1
	for j in range(1,(n-mid+1)):
		if(max_length(f,maxx)):
			x=1
			break

		f[ord(s[j-1])-ord('a')]-=1
		f[ord(s[j+mid-1])-ord('a')]+=1

	if(max_length(f,maxx)):
		x=1
	if(x):
		ans=mid
		high=mid-1
	else:
		low=mid+1

print(ans)
