import sys
filename = sys.argv[0]
f_in = open('fizz_buss_in.txt', 'r')
f_out = open('fizz_buss_out.txt', 'w')
for i in range(20):
    c=f_in.readline()
    f,b,n=c.split()
    f=int(f)
    b=int(b)
    n=int(n)
    for i in range(1,n+1):
        if i%f==0 and i%b==0:
            print('FB',end=' ',file=f_out)
        elif not i%f:
            print('F',end=' ',file=f_out)
        elif not i%b:
            print('B',end=' ',file=f_out)
        else:
            print(i, end=' ',file=f_out)
    print('\t',file=f_out)

f_in.close()
f_out.close()
