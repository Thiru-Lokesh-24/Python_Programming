n=int(input("Enter number : "))
target=""

if n>=10000 and n<=99999:
    for i in range(len(str(n))-1):
        if chr(n[i]+n[i+1]) in chr(n) or chr(n[i]-n[i+1]) in chr(n):
            target=1
else:
    print("This number is not convert to monopoly")