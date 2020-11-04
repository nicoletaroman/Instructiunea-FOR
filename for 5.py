s=0
n=eval(input("dati un nr"))
for nr in range(1,n+1):
    if nr%5==0 and nr%3==0:
        s=nr+s
        print("suma este",s)