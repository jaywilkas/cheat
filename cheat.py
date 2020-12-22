#!/usr/bin/python

'''
Minimalist "https://cheat.sh" and "tldr" - client
'''

import sys
import pycurl
from io import BytesIO



buffer = BytesIO()
crl = pycurl.Curl()
crl.setopt(crl.URL, 'https://cheat.sh/' + '/'.join(sys.argv[1:]))
crl.setopt(crl.WRITEDATA, buffer)
crl.perform()
crl.close()

body = buffer.getvalue().decode('utf8')

tldr_encountered = False
for line in body.split('\n'):
    if line[15:20]  == 'tldr:':
        tldr_encountered = True
    print(line)

if not tldr_encountered:
    CSI = "\x1B["
    print(f'{CSI}48;5;8m{CSI}24m tldr:{" ".join(sys.argv[1:])} {CSI}24m{CSI}0m')

    import re
    from tldr import cli
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(cli())

