n=int(input())
num=list(map(int,input().split()))
b={}
a=[]
for i in num:
   b[i]=b.get(i,0)+1
max_bansh=max(b.values())
key=[k for k,v in b.items() if v==max_bansh] 
a.append(key)
print(min(min(a)))
