http://10.10.207.21:31337/
EASY PESY
In case I forget - user:pass
ubuntu:Dafdas!!/str0ng

root@ip-10-10-251-129:~# ssh ubuntu@10.10.207.21
The authenticity of host '10.10.207.21 (10.10.207.21)' can't be established.
ECDSA key fingerprint is SHA256:tD+Aiagv/4teueystsEl6q9ZNvNF9C8v+dsZj3fhbdQ.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.10.207.21' (ECDSA) to the list of known hosts.
ubuntu@10.10.207.21's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.13.0-1014-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

$ ls
$ whoami
ubuntu
$ ls
$ cd
$ pwd
/home/ubuntu
$ cd /root
-sh: 6: cd: can't cd to /root
$ ls
$ pw
-sh: 8: pw: not found
$ pwd
/home/ubuntu
$ cd ..
$ ls
ubuntu	user
$ cd user
$ ls
flag.txt
$ cat flag.txt
flag{251f309497a18888dde5222761ea88e4}$ 
