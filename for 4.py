a=eval(input("dati un nr"))
b=eval(input("dati un nr"))
for nr in range(a,b+1):
    if nr%2!=0:
        print(nr,end=" ,")