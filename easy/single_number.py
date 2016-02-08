import util

import sys

tr = util.TokenReader(sys.stdin)

try:
    xor = 0
    
    while True:
        n = int(next(tr))
    
        if n == -1:
            break
    
        xor ^= n
    
    print xor
except:
    print >>sys.stderr, 'Wrong input format. Terminating...'
    sys.exit(1)
