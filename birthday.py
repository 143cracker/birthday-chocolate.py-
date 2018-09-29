n=int(input())
b=list(map(int,input().split()))
dm=list(map(int,input().split()))
count=0
if n==1 and b[0]==dm[0]:
        count=count+1
elif n==1 and b[0]==0 and dm[0]==0:
    count=0
for i in range((len(b)-1)):
    if sum(b[i:dm[1]+i])==dm[0]:
            count=count+1
  
    else:pass

print(count)
