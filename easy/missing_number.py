import util

import sys

tr = util.TokenReader(sys.stdin)

try:
    sum_ = 0
    n_max = 0
    while True:
        n = int(next(tr))
        if n == -1:
            break
        sum_ += n
        if n > n_max:
            n_max = n
    k = n_max * (n_max + 1) / 2 - sum_
    if k == 0:
        k = n_max + 1

    print k
    

except:
    print >>sys.stderr, 'Wrong input format. Terminating...'
    sys.exit(1)
