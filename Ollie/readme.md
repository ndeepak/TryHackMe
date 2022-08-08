Ollie Machine
Link: https://tryhackme.com/room/ollie
IP: 10.10.65.123 

## NMAP:
# Nmap 7.92 scan initiated Wed Aug  3 05:07:35 2022 as: nmap -sC -sV -vv -oN nmap ollie
```
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-robots.txt: 2 disallowed entries 
|_/ /immaolllieeboyyy
| http-title: Ollie :: login
|_Requested resource was http://ollie/index.php?page=login
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)

```
nmap -sC -sV ollieshouse.thm -p 22,80,1337 -vv -oN specPortScan
```
Nmap scan report for ollieshouse.thm (10.10.65.123)
PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| http-title: Ollie :: login
|_Requested resource was http://ollieshouse.thm/index.php?page=login
| http-robots.txt: 2 disallowed entries 
|_/ /immaolllieeboyyy
|_http-favicon: Unknown favicon MD5: 851615F43921F017A297184922B4FBFD
1337/tcp open  waste?  syn-ack
| fingerprint-strings: 
|   DNSStatusRequestTCP, GenericLines: 
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up, 
|     It's been a while. What are you here for?
|   DNSVersionBindReqTCP: 
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up, 
|     version
|     bind
|     It's been a while. What are you here for?
|   GetRequest: 
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up, Get / http/1.0
|     It's been a while. What are you here for?
|   HTTPOptions: 
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up, Options / http/1.0
|     It's been a while. What are you here for?
|   Help: 
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up, Help
|     It's been a while. What are you here for?
|   NULL, RPCCheck: 
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name?
|   RTSPRequest: 
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up, Options / rtsp/1.0
|_    It's been a while. What are you here for?

```


## RUSTSCAN
rustscan -a ollieshouse.thm -b 100 --ulimit 100
```
Open 10.10.65.123:22
Open 10.10.65.123:80
Open 10.10.65.123:1337
```
## Telnet 1337
```
└─$ telnet ollieshouse.thm 1337                                              
Trying 10.10.65.123...
Connected to ollieshouse.thm.
Escape character is '^]'.
Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
What is your name? obscure
! It's been a while. What are you here for? hack
. If you can answer a question about me, I might have something for you.
What breed of dog am I? I'll make it a multiple choice question to keep it easy: Bulldog, Husky, Duck or Wolf? Bulldog
You are correct! Let me confer with my trusted colleagues; Benny, Baxter and Connie...
Please hold on a minute
Ok, I'm back.
After a lengthy discussion, we've come to the conclusion that you are the right person for the job.Here are the credentials for our administration panel.
                    Username: admin
                    Password: Hello World <-- OllieUnixMontgomery! -->

PS: Good luck and next time bring some treats!
Connection closed by foreign host.
```
## Gobuster-Directory
```

```

Juicy Site: https://github.com/phpipam/phpipam


Hash+Salt 
```
$6$rounds=3000
$JQEE6dL9NpvjeFs4$RK5X3oa28.Uzt/h5VAfdrsvlVe.7HgQUYKMXTJUsud8dmWfPzZQPbRbk8xJn1Kyyt4.dWm4nJIYhAV2mbOZ3g.
```
