num=list(map(int,input("Enter Your Number: ").split()))
num.sort()
final=[]
first=num[:len(num)//2]
last=num[len(num)//2:]
last.reverse()
for i in range (len(first)):
    final.append(last[i])
    final.append(first[i])
if(len(first)==len(last)):
    pass
else:
    final.append(last[-1])
print(final)