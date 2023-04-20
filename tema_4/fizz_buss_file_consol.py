import sys
filename = sys.argv[0]
f_in = open('fizz_buss_in.txt', 'r')
for i in range(20):
    c=f_in.readline()
    f,b,n=c.split()
    f=int(f)
    b=int(b)
    n=int(n)
    for i in range(1,n+1):
        if i%f==0 and i%b==0:
            print('FB',end=' ')
        elif not i%f:
            print('F',end=' ')
        elif not i%b:
            print('B',end=' ')
        else:
            print(i, end=' ')
    print('\t')
f_in.close()

