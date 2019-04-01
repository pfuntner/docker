#! /usr/bin/env python

import sys
import json
import subprocess

ips = {}
for container in ['ansible', 'vanilla1', 'vanilla2']:
  # don't do the two vanilla containers if any arguments are passed in on the command line
  if (len(sys.argv) == 1) or (container == 'ansible'):
    p = subprocess.Popen(['docker', 'inspect', container], stdout=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    rc = p.wait()
    assert (rc == 0) and stdout
    ips[container] = json.loads(stdout)[0]['NetworkSettings']['IPAddress']

with open('ips.json', 'w') as stream:
  json.dump(ips, stream)
