#! /usr/bin/env python

import sys
import time
import datetime

pgm = sys.argv[0]
with open('/tmp/waiter.log', 'w') as stream:
  while True:
    now = datetime.datetime.now()
    msg = '{pgm} running at {now}'.format(**locals())
    stream.write('{msg}\n'.format(**locals()))
    stream.flush()
    print msg
    time.sleep(60**2)
