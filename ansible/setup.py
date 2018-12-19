#! /usr/bin/env python

import os
import re
import sys
import pwd
import json
import subprocess

def run(cmd):
  subprocess.Popen(cmd.split()).wait()

def add_to_known_hosts(user):
  print 'Adding to .ssh/known_hosts for {user}'.format(**locals())
  for host in ['localhost', 'ansible', 'vanilla1', 'vanilla2']:
    run('ssh {host} -o StrictHostKeyChecking=no true'.format(**locals()))

def customize_profiles(user):
  print 'Customizing {user}\'s profiles'.format(**locals())
  with open('.profile', 'a') as stream:
    stream.write('export PAGER=less\n')
    stream.write('export EDITOR=vi\n')

  with open('.bashrc', 'a') as stream:
    stream.write('set -o vi\n')
    stream.write('alias more=less\n')
    stream.write('alias br="vi -R"\n')
    stream.write('alias r="fc -s"\n')

ips = {}
with open('/tmp/ips.json') as stream:
  ips = json.load(stream)

print '\nAdding {ips} to /etc/hosts'.format(**locals())
with open('/etc/hosts', 'a') as stream:
  for (host, ip) in ips.items():
    stream.write('{ip} {host}\n'.format(**locals()))

add_to_known_hosts('root')
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
add_to_known_hosts('peon')
customize_profiles('peon')
