import sys
b=[]
filename = sys.argv[0]
f = open(filename, 'r') 
for line in f: 
	b+=line
for i in b[::-1]:
    print(i,end='')
f.close() 
