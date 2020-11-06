n=eval(input("Introdu n:"))
s=0

for i in range(0, n+1):
    if ((i%3==0)and(i%5==0)):
        s+=i
print(s)