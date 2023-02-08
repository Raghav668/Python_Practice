a = 0
b = 1
inp = int(input("Enter the number to provide fibbonci series"))
print(a,b, end =" ")
for i in range(1,inp):
    c = a+b
    a=b
    b=c
    print(c,end = " ")


    #prime number
a=2
number = int(input("Enter the number to provide sequence of prime numbers"))

for num in range(a,number+1):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
                print(num)



