## Web Enumeration
Learn the methodology of enumerating websites by using tools such as Gobuster, Nikto and WPScan
Link: https://tryhackme.com/room/webenumerationv2

[Gobuster](GobusterManual.docx)

## Task 6
```
Q) Run a directory scan on the host. Other than the standard css, images and js directories, what other directories are available?
// [GobusterScan](task6gobuster.txt)

Q) Run a directory scan on the host. In the "C******" directory, what file extensions exist?
// gobuster dir -u webenum.thm/changes -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x.html,.css,.js,.php,.asp,.txt,.conf,.config


Q) There's a flag out there that can be found by directory scanning! Find it!
// gobuster dir -u webenum.thm/Changes -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x.html,.css,.js,.php,.asp,.txt,.conf,.config,.flag


Q) There are some virtual hosts running on this server. What are they?
//  gobuster vhost -u http://webenum.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt 


Q) There's another flag to be found in one of the virtual hosts! Find it!
    root@ip-10-10-83-98:~# echo "10.10.56.83 learning.webenum.thm" >> /etc/hosts
    root@ip-10-10-83-98:~# echo "10.10.56.83 products.webenum.thm" >> /etc/hosts

 gobuster dir -u http://vhosts.webenum.thm/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x.html,.css,.js,.php,.asp,.txt,.conf,.config

```
```
Enumerate the site, what is the name of the theme that is detected as running?
wpscan --url http://wpscan.thm/ --enumerate t 

WPScan says that this theme is out of date, what does it suggest is the number of the latest version?
 Same as above

Enumerate the site, what is the name of the plugin that WPScan has found?
 wpscan --url http://wpscan.thm/ --enumerate p

Enumerate the site, what username can WPScan find?
 wpscan --url http://wpscan.thm/ --enumerate u


Construct a WPScan command to brute-force the site with this username, using the rockyou wordlist as the password list. What is the password to this user? 
 wpscan --url http://wpscan.thm/ --username <name> --password /usr/share/wordlists/rockyou.txt 

```

<!-- Enumerate the site, what is the name of the theme that is detected as running?
twentynineteen
WPScan says that this theme is out of date, what does it suggest is the number of the latest version?

2.3
Enumerate the site, what is the name of the plugin that WPScan has found?

nextgen-gallery
Enumerate the site, what username can WPScan find?

phreakazoid
Construct a WPScan command to brute-force the site with this username, using the rockyou wordlist as the password list. What is the password to this user? 

linkinpark -->

```
What is the name & version of the web server that  Nikto has determined running on port 80?
nikto -h <IP>:80

There is another web server running on another port. What is the name & version of this web server?
same as above:8080

What is the name of the Cookie that this JBoss server gives?
nikto -h <IP>:<port> -Display 2
```


<!-- What is the name & version of the web server that  Nikto has determined running on port 80?
Apache/2.4.7
There is another web server running on another port. What is the name & version of this web server?

Apache-Coyote/1.1
What is the name of the Cookie that this JBoss server gives?

JSESSIONID -->
