import sys

try:
    n = int(raw_input())
except:
    print 'Incorrect value'
    sys.exit(1)

res = n # n**1
n2 = n * n
res = res * n2 # n**3
n4 = n2 * n2
n8 = n4 * n4
res = res * n8 # n**11
n16 = n8 * n8
res = res * n16 # n**27
n32 = n16 * n16
res = res * n32 # n**59

print res
