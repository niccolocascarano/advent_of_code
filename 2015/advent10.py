#!/usr/bin/python

i = '1113122113'

for m in range(1, 51):
    idx = 0
    cur_char = None
    cur_char_count = 0
    new = []
    while idx < len(i):
        if not cur_char:
            cur_char = i[idx]
            cur_char_count = 1
        if idx < len(i)-1 and i[idx+1] == cur_char:
            cur_char_count += 1
        else:
            new.append(str(cur_char_count))
            new.append(cur_char)
            cur_char = None
        idx += 1

    i = ''.join(new)
    if m == 40 or m == 50:
        print 'Total lenght at %d: %d' % (m, len(i))
    
