# Ansible container
I originally created this to mess with Ansible from a Linux machine.  I think I finally did find a real Linux machine on which I could run Ansible but I still can use this to experiment with Ansible and learn more bout it.

Basically what I wanted was a Linux container that would stay up and to which I could attach to get to the shell.

## Usage
When I first created this procedure, I would run this from a Cygwin shell on Windows 10 but I imagine it would work from Linux as well.  If you run `make`, it will build the image, start the containers (in which Python process runs forever to keep each container up.), and remind you how to `docker exec` into the main container to start a new shell.

<span style="color:red;">This must be **not** be done from a host Cygwin shell.  It can be done from a basic Windows command prompt, though.</span>

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

root@ansible:~#
```

## Issues
There are some issues with this:
* The biggest issue is that I never got networking working correctly.  I can ping sites on the internet by their dotted address but not by hostname so I guess it's a DNS issue but I still haven't found a solution.
  * The reason for wanting DNS working is because the container still doesn't have Ansible installed.  I am not able to install Ansible because I can't reach the outside work from inside the container.
