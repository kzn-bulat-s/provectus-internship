"""
    
"""

import util

import sys

tr = util.TokenReader(sys.stdin)

try:
    a, b, c = [float(tr.next()) for _ in xrange(3)]
    x, y, z = [0., 0., 0.] # buffers 
    while True:
        x, y = y, z
        z = float(next(tr))
        
        if z == 0:
            coeff_prev = y * b + a * x
            coeff_last = y * a
            print coeff_prev, coeff_last
            break

        coeff = z * c + y * b + a * x
        print coeff,
        
except (StopIteration, ValueError):
    print >>sys.stderr, 'Wrong input format. Terminating...'
    sys.exit(1)
