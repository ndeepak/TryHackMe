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
