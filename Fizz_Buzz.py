f=int(input("please give me a fizz: "))
b=int(input("please give me a buzz: "))
n=int(input("please give me a number: "))
for i in range(1,n+1):
    if i%f==0 and i%b==0:
        print('FB',end=' ')
    elif not i%f:
        print('F',end=' ')
    elif not i%b:
        print('B',end=' ')
    else:
        print(i, end=' ')

