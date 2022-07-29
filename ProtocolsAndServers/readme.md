# Ports and Server Room

https://tryhackme.com/room/protocolsandservers

NMAP Scan:

```
root@ip-10-10-194-17:~# nmap 10.10.176.238
Starting Nmap 7.60 ( https://nmap.org ) at 2022-07-29 12:16 BST
Nmap scan report for ip-10-10-176-238.eu-west-1.compute.internal (10.10.176.238)
Host is up (0.0012s latency).
Not shown: 992 closed ports
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
25/tcp  open  smtp
80/tcp  open  http
110/tcp open  pop3
143/tcp open  imap
993/tcp open  imaps
995/tcp open  pop3s
MAC Address: 02:92:3E:57:1A:91 (Unknown)
```
## HTTP
```
root@ip-10-10-194-17:~# nmap 10.10.176.238

Starting Nmap 7.60 ( https://nmap.org ) at 2022-07-29 12:16 BST
Nmap scan report for ip-10-10-176-238.eu-west-1.compute.internal (10.10.176.238)
Host is up (0.0012s latency).
Not shown: 992 closed ports
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
25/tcp  open  smtp
80/tcp  open  http
110/tcp open  pop3
143/tcp open  imap
993/tcp open  imaps
995/tcp open  pop3s
MAC Address: 02:92:3E:57:1A:91 (Unknown)
```
## TELNET
```
┌──(kali㉿kali)-[~]
└─$ telnet 10.10.176.238 80
Trying 10.10.176.238...
Connected to 10.10.176.238.
Escape character is '^]'.
GET /flag.thm HTTP/1.1
host:telnet

HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Fri, 29 Jul 2022 12:09:43 GMT
Content-Type: application/octet-stream
Content-Length: 39
Last-Modified: Wed, 15 Sep 2021 09:19:23 GMT
Connection: keep-alive
ETag: "6141ba9b-27"
Accept-Ranges: bytes

THM{**********}
```

## FTP
