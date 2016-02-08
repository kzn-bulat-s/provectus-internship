import util

import sys

tr = util.TokenReader(sys.stdin)

try:
    candidate = None
    count = 0
    while True:
        n = int(tr.next())
        
        if n == -1:
            break

        if count == 0:
            candidate = n
            count = 1
        elif candidate == n:
            count += 1
        else:
            count -= 1

    print candidate
except:
    print >>sys.stderr, 'Wrong input format. Terminating'
