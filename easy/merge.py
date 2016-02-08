import sys

try:
    data = map(int, sys.stdin.read().split())

    n = data[0]
    m = data[n+1]

    a_iter = iter(data[1:n+1])
    b_iter = iter(data[n+2:n+m+2])
except:
    print >>sys.stderr, 'Wrong input format. Terminating...'
    sys.exit(1)
     
union = []
intersect = []
except_ = []    

a_val = None
b_val = None

try:
    a_val = next(a_iter)
    b_val = next(b_iter)
    while True:
        if a_val < b_val:
            union.append(a_val)
            except_.append(a_val)
            a_val = next(a_iter)
        elif a_val > b_val:
            union.append(b_val)
            b_val = next(b_iter)
        else:
            union.append(a_val)
            intersect.append(a_val)
            a_val = next(a_iter)
            b_val = next(b_iter)
except:
    pass

try:
    while True:
        a_val = next(a_iter)
        union.append(a_val)
        except_.append(a_val)
except:
    pass

try:
    while True:
        b_val = next(b_iter)
        union.append(b_val)
except:
    pass

print 'UNION:', ' '.join(map(str, union))
print 'INTERSECT:', ' '.join(map(str, intersect))
print 'EXCEPT:', ' '.join(map(str, except_))
