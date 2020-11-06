s5=0
n=eval(input("Introdu n:"))
for x in range(1, n+1):
    s5=s5+(x/(x+1))
print("s5= ", round(s5, 2))