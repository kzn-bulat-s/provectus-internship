import sys
import re
import codecs

sys.stdin = codecs.getreader('utf8')(sys.stdin)
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

# Uses tip from this answer: http://stackoverflow.com/a/8923989
expr = re.compile(r'([^\W\d_]+)', flags=re.UNICODE)

last = ''
lastButOne = '-'

for line in sys.stdin:
    for i, chunk in enumerate(expr.split(line)):
        if i & 1:
            if last == lastButOne:
                if chunk[0].isupper() and chunk[-1].islower():
                    new_chunk = list(chunk)
                    new_chunk[0] = chunk[0].lower()
                    new_chunk[-1] = chunk[-1].upper()
                    sys.stdout.write(''.join(new_chunk[::-1]))
                else:
                    sys.stdout.write(chunk[::-1])
            else:
                sys.stdout.write(chunk)       
            lastButOne = last
            last = chunk.lower()
        else:
            sys.stdout.write(chunk)

sys.stdout.close()
