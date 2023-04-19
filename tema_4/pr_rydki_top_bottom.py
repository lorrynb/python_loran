import sys
a=[]
filename = sys.argv[0]
f = open(filename, 'r') 
for line in f: 
	a+=line[::-1]
for i in a[::-1]:
    print(i,end='')
f.close() 
