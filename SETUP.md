# User
## Create user
adduser pyshell
## Edit /etc/passwd
Change the shell from /bin/bash to /usr/bin/pyshell.py

# SSHD Setup
## /etc/ssh/sshd_config edits
Add to the end of the file

Match User pyshell
        PermitEmptyPasswords yes
        AllowTcpForwarding no
        X11Forwarding no
        Banner /etc/ssh/user-pyshell

## /etc/ssh/user-pyshell
Edit the file to contain what ever you want to show on intial pyshell login

  ###################################################
                       PyShell
  ###################################################