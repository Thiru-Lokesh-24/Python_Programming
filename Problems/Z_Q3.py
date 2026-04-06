num=list(map(int,input("Enter numbers : ").split()))
even=list(i for i in num if i%2==0)
odd=list(i for i in num if i%2==1)
even.sort()
odd.reverse()
final=[]
for i in range(len(num)):
    try:
        final.append(odd[i])
        final.append(even[i])
    except IndexError:
        pass
print(final)