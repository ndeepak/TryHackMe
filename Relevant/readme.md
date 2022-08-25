# Relevant
Link: https://tryhackme.com/room/relevant


[NMAP SCAN](nmap.txt)

 smbclient -L 10.10.39.64
WARNING: The "syslog" option is deprecated
Enter WORKGROUP\root's password: 

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	nt4wrksv        Disk      
Reconnecting with SMB1 for workgroup listing.
Connection to 10.10.39.64 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Failed to connect with SMB1 -- no workgroup available
root@ip-10-10-74-21:~# 

root@ip-10-10-74-21:~# smbclient \\\\10.10.39.64\\nt4wrksv
WARNING: The "syslog" option is deprecated
Enter WORKGROUP\root's password: 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sat Jul 25 22:46:04 2020
  ..                                  D        0  Sat Jul 25 22:46:04 2020
  passwords.txt                       A       98  Sat Jul 25 16:15:33 2020

		7735807 blocks of size 4096. 4950520 blocks available
smb: \> cat passwords.txt
cat: command not found
smb: \> get
get <filename> [localname]
smb: \> get passwords.txt
getting file \passwords.txt of size 98 as passwords.txt (0.3 KiloBytes/sec) (average 0.3 KiloBytes/sec)
smb: \> 
smb: \> pwd
Current directory is \\10.10.39.64\nt4wrksv\
smb: \> exit
root@ip-10-10-74-21:~# ls
Desktop    Instructions   Pictures  Rooms    thinclient_drives
Downloads  passwords.txt  Postman   Scripts  Tools
root@ip-10-10-74-21:~# cat passwords.txt 
[User Passwords - Encoded]
Qm9iIC0gIVBAJCRXMHJEITEyMw==
QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQk

root@ip-10-10-74-21:~# 
