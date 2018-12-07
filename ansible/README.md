# Ansible container
I originally created this to mess with Ansible from a Linux machine but I didn't get very far with it.  Eventually, I found a machine with Ansible already installed on which I also had `sudo` ability so I'm going to use that.

Basically what I wanted was a Linux container that would stay up and to which I could attach to get to the shell.

## Usage
I would run this from Windows 10 but I imagine it would work from Linux as well.  If you run `make`, it will build the image, start the container, and remind you how to `docker exec` into it to start a new shell - this must be **not** be done from a host cygwin shell.  It can be done from a basic Windows command prompt, though.  A Python process starts when you start the container which keeps the container up.

## Issues
There are some issues with this:
* The biggest issue is that I never got networking working correctly.  I can ping sites on the internet by their dotted address but not by hostname so I guess it's a DNS issue but I still haven't found a solution.
** The reason for wanting DNS working is because the container still doesn't have Ansible installed.
