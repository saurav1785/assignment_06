#Question 1
#Answer
pi=3.14
def area(r):
    return (4*3.14*r**2)
radius=int(input('Enter the radius:'))
ans=area(radius)
print(ans)

#Question 2
#Answer

print('Perfect Numbers:')
def perfect(num):
    summ=0
    for i in range(1,num):
        if(num%i==0):
            summ=summ+i
    if(summ==num):
        print(num)
for x in range(1,1000):
    perfect(x)

#Question 3
#Answer

def table(n):
    for x in range(1,11):
        print(n*x)
num=int(input('Enter the no.:'))
table(num)

#Question 4
#Answer

def power(c,b):
    if(b==1):
        return c
    else:
        return c*power(c,b-1)
num1=int(input('Enter number'))
num2=int(input('Enter exponent'))
r=power(num1,num2)
print('Result: ',r)
print(c)
