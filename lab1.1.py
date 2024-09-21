a = int(input("Enter a:"))
b = int(input("Enter b:"))
while a<1 or a>100:
    a = int(input("Enter a:"))

while b<1 or b>100:
 b = int(input("Enter b one more time:"))
if a>b:
    X=(a*a-b)
elif a==b:
    X=(-a)
else:
    X=(a*b-1)/b
    print("Result of the problem: ",X)
    