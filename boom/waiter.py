#! /usr/bin/env python

import sys
import time
import random
import logging
import argparse

parser = argparse.ArgumentParser(description=sys.argv[0])
parser.add_argument('seconds', type=int, nargs='?', help='Number of seconds to sleep')
args = parser.parse_args()

logging.basicConfig(format='%(asctime)s %(levelname)s %(pathname)s:%(lineno)d %(msg)s')
log = logging.getLogger()
log.setLevel(logging.DEBUG)

if not args.seconds:
  args.seconds = random.randint(60, 5*60)

log.debug('Started, sleeping for {args.seconds} seconds'.format(**locals()))
time.sleep(args.seconds)
log.debug('Raising exception')

raise Exception('Good bye, cruel world!')
