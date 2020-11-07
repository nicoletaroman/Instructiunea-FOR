s1=0
s2=0
s3=0
s4=0
s5=0
s6=0
n1=eval(input("dati un nr"))
n2=eval(input("dati un nr"))
n3=eval(input("dati un nr"))
n4=eval(input("dati un nr"))
n5=eval(input("dati un nr"))
n6=eval(input("dati un nr"))
for nr in range(1,n1+1):
    s1+=nr
for nr in range(2,n2+1):
    s2+=(nr-1)*nr
for nr in range(1,n3+1):
    m=1
    for i in range(1,nr+1):
        m*=i
    s3+=m
for nr in range(1,n4+1):
    s4+=nr*10+2
for nr in range(1,n5+1):
    s5+=nr/(nr+1)
for nr in range(2,n6+1):
    if nr<10:
        s6+=20+nr
        S6=s6+1+2
    else:
        s6+=20*(10**(nr//10))+nr
    
print("s1=",s1)
print("s2=",s2)
print("s3=",s3)
print("s4=",s4)
print("s5=",s5)
print("s6=",S6)

