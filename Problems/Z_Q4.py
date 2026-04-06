num=int(input("Enter numer :"))
l=len(str(num))
while True:   
    if chr(num+64)>="A" and chr(num+64)<="Z":
        print(chr(num+64)*l)
        break
    else:
        num=num-26          