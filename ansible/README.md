# Ansible container
I originally created this to mess with Ansible from a Linux machine.  I think I finally did find a real Linux machine on which I could run Ansible but I still can use this to experiment with Ansible and learn more bout it.

Basically what I wanted was a Linux container that would stay up and to which I could attach to get to the shell.

## Usage
When I first created this procedure, I would run this from a Cygwin shell on Windows 10 but I imagine it would work from Linux as well.  If you run `make`, it will build the image, start the containers (in which Python process runs forever to keep each container up.), and remind you how to `docker exec` into the main container to start a new shell.

**This must be not be done from a host Cygwin shell.**  It can be done from a basic Windows command prompt, though.</span>

## Adhoc commands
```
root@ansible:~# grep -vE '^(#|$)' /etc/ansible/hosts # This file is populated by the setup procedure
vanilla1
vanilla2
root@ansible:~# ansible all -m ping
vanilla1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
vanilla2 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
root@ansible:~# ansible all -m command -a uptime
vanilla2 | SUCCESS | rc=0 >>
 14:39:59 up  2:51,  1 user,  load average: 0.00, 0.00, 0.00

vanilla1 | SUCCESS | rc=0 >>
 14:39:59 up  2:51,  1 user,  load average: 0.00, 0.00, 0.00

root@ansible:~# ansible vanilla1 -m setup | headtail -30
       1 vanilla1 | SUCCESS => {
       2     "ansible_facts": {
       3         "ansible_all_ipv4_addresses": [
       4             "172.17.0.3"
       5         ],
       6         "ansible_all_ipv6_addresses": [],
       7         "ansible_architecture": "x86_64",
       8         "ansible_bios_date": "03/02/2018",
       9         "ansible_bios_version": "Hyper-V UEFI Release v3.0",
      10         "ansible_cmdline": {
      11             "BOOT_IMAGE": "/boot/kernel",
      12             "console": "ttyS0",
      13             "page_poison": "1",
      14             "panic": "1",
      15             "root": "/dev/sr0",
         .
         .
         .
     318         "ansible_uptime_seconds": 12615,
     319         "ansible_user_dir": "/root",
     320         "ansible_user_gecos": "root",
     321         "ansible_user_gid": 0,
     322         "ansible_user_id": "root",
     323         "ansible_user_shell": "/bin/bash",
     324         "ansible_user_uid": 0,
     325         "ansible_userspace_architecture": "x86_64",
     326         "ansible_userspace_bits": "64",
     327         "ansible_virtualization_role": "guest",
     328         "ansible_virtualization_type": "docker",
     329         "module_setup": true
     330     },
     331     "changed": false
     332 }
root@ansible:~# ansible vanilla2 -m command -a 'date +%Y%m%d'
vanilla2 | SUCCESS | rc=0 >>
20190329
root@ansible:~#
```
Note: [`headtail`](https://github.com/pfuntner/toys/blob/master/bin/headtail) is a command of mine own that is not found on \*ix machines

## Issues
There are some issues with this:
* The biggest issue is that I never got networking working correctly.  I can ping sites on the internet by their dotted address but not by hostname so I guess it's a DNS issue but I still haven't found a solution.
  * The reason for wanting DNS working is because the container still doesn't have Ansible installed.  I am not able to install Ansible because I can't reach the outside work from inside the container.
