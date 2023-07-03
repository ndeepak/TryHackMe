# Anthem 
Exploit a Windows machine in this beginner level challenge.
https://tryhackme.com/room/anthem

All the answers are in Task*.txt files. [File1](Task1.txt) [File2](Task2.txt) [File3](Task3.txt)

Steps:

* Run the Nmap Scan
└─# sudo nmap -A -sC -sV -p- -Pn -T4 10.10.52.153
```
80/tcp   open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
```

Tasks 1
```
* Run namp
* See robots.txt
* Use Wappalyzer in login page
* Home Page
* Search for the poem in google
* Resume/CV page like email
```

Tasks 2
```
* Find it in the source code of the various files.
1st one at view-source:http://10.10.52.153/archive/we-are-hiring/
2nd one at view-source:http://10.10.52.153/
3rd one at http://10.10.52.153/authors/jane-doe/
4th one at view-source:http://10.10.52.153/archive/a-cheers-to-our-it-department/
```

Tasks 3
```
Take remote desktop as from Nmap scan
 cmd: xfreerdp /v:<ip> /u:sg /p:Password /cert:ignore +clipboard /dynamic-resolution

* Search for the text file in user desktop only 
* Admin password is in Hidden in C:\..\ folder with 1 byte or something.
* Change that file security setting, add yourself (sg user) and give full acccess.

* Now with that password, again use xfreerdp to access administrator and access text files.

```