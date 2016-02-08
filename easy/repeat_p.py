import util

import sys

tr = util.TokenReader(sys.stdin)

N_BINS = 50

try:
    p = int(tr.next())
    counts = [0] * N_BINS
    while True:
        n = int(tr.next())
        
        if n == -1:
            break

        for i in xrange(N_BINS):
            if (n >> i) & 1:
                counts[i] += 1
                if counts[i] == p:
                    counts[i] == 0
    
    result = 0
    for i in xrange(N_BINS):
        if counts[i] != 0:
            result |= (1<<i)

    print result
except:
    print >>sys.stderr, 'Wrong input format. Terminating...'
