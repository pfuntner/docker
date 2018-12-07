#! /usr/bin/env python

import sys
import time
import datetime

pgm = sys.argv[0]
now = datetime.datetime.now()
msg = '{pgm} started at {now}'.format(**locals())
print msg
with open('waiter.log', 'w') as stream:
  stream.write('{msg}\n'.format(**locals()))

time.sleep(2**32)
