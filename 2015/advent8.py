#!/usr/bin/python

import re

f = open('advent8')

text = 0
enc_text = 0
code = 0
for line in f:
    line = line.strip()
    text += len(line)
    lc = 0

    encoded_line = str(line)
    encoded_line = re.sub(r'\\','\\\\\\\\', encoded_line)
    encoded_line = re.sub(r'"','\\"', encoded_line)
    encoded_line = '"' + encoded_line + '"'
    enc_text += len(encoded_line)
    print '%s -> %s' % (line, encoded_line)
    escape = False
    for c in line:
        if c == '"' and not escape:
            continue
        if c == '\\' and not escape:
            escape = True
            continue
        if c == 'x' and escape:
            escape = False
            lc -= 1
            continue
        escape = False
        lc += 1
    code += lc


print 'Text is %d' % text
print 'Enc Text is %d' % enc_text
print 'Code is %d' % code
print 'Delta is %d' % (text - code)
print 'Delta enc is %d' % (enc_text - text)
