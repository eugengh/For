a=eval(input("a= "))
b=eval(input("b= "))
if a%2!=0:
    for x in range(a, b+1, 2):
        print(x, end=" ")
elif a%2==0:
    for b in range(a+1, b+1, 2):
        print(b, end=" ")