n=int(input("dati un numar:"))
s=0
for i in range(1,n+1):
    if (i%3==0) and (i%5==0):
        s+=i
print("suma este =",s)