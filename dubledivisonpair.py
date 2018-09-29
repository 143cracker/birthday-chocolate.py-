n=list(map(int,input().split()))
shivam=list(map(int,input().split()))
count=0
for i in range(0,len(shivam)):
    for j in range (1,len(shivam)):
          if i<j:
             if (shivam[i]+shivam[j])%n[1]==0 :
                  count=count+1
print(count)
       
