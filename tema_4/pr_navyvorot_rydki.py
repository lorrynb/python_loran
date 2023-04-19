import sys
a=[]
filename = sys.argv[0]
f = open(filename, 'r') 
for line in f: 
	a+=line[::-1]
for i in a:
    print(i,end='')
f.close() 
