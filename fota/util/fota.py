#!/usr/bin/env python

import sys
old = sys.argv[1]
new = sys.argv[2]
data = open(old, 'rb').read()
start = data.find('PK')

end = 0
while True:
    #  0xff 0xff \xXX \xXX end
    # -4   -3   -2   -1   0 
    if data[end-4:end-2] == '\xff\xff':
        break
    end -= 1

with open(new, 'wb') as w:
    if end == 0:
        w.write(data[start:])
    else:
        w.write(data[start:end])
