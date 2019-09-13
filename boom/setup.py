#! /usr/bin/env python

import os
import re
import sys
import pwd
import json
import subprocess

def run(cmd):
  subprocess.Popen(cmd.split()).wait()

def customize_profiles(user):
  print 'Customizing {user}\'s profiles'.format(**locals())
  with open('.profile', 'a') as stream:
    stream.write('export PAGER=less\n\n')
    stream.write('export EDITOR=vi\n')
    stream.write('PATH=$PATH:/root/bin\n')

  with open('.bashrc', 'a') as stream:
    # repeat environment variables from .profile because .profile isn't run when you use `docker exec -it ansible bash`
    stream.write('export PAGER=less\n\n')
    stream.write('export EDITOR=vi\n')
    stream.write('PATH=$PATH:/root/bin\n\n')

    # these are just for .bashrc
    stream.write('set -o vi\n')
    stream.write('alias more=less\n')
    stream.write('alias r="fc -s"\n')

run('chmod a+rx /root')
customize_profiles('root')

print 'Creating user peon'
p = subprocess.Popen('adduser peon'.split(), stdin=subprocess.PIPE)
(stdout, stderr) = p.communicate()
p.wait()

print 'Creating /home/peon/.ssh structure'
os.mkdir('/home/peon/.ssh')
for filename in ['id_rsa', 'id_rsa.pub', 'authorized_keys']:
  run('cp -v /root/.ssh/{filename} /home/peon/.ssh/'.format(**locals()))
run('chown -Rv peon /home/peon/.ssh')
run('chmod -Rv 700 /home/peon/.ssh')

print 'Granting peon the ability to use sudo'
run('usermod -a -G sudo peon')

print 'Enabling peon to use sudo without a password'
regexp = re.compile(r'^%sudo\s+ALL=\(ALL:ALL\)\s+ALL')
with open('/etc/sudoers.new', 'w') as newfile:
  with open('/etc/sudoers', 'r') as oldfile:
    for line in oldfile:
      if regexp.search(line):
        line = '%sudo\tALL=(ALL:ALL) NOPASSWD: ALL\n'
      newfile.write(line)
run('mv -v /etc/sudoers /etc/sudoers.old')
run('mv -v /etc/sudoers.new /etc/sudoers')

peon = pwd.getpwnam('peon').pw_uid
print 'peon uid is {peon}'.format(**locals())

os.setuid(peon)
os.chdir('/home/peon')
customize_profiles('peon')
