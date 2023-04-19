import sys
filename = sys.argv[0]
f_in = open('fizz_buss_in.txt', 'r')
f_out = open('fizz_buss_out.txt', 'w')
for line in f_in:
    print(line, end='')
    f_out.write(line)
f_in.close()
f_out.close()
