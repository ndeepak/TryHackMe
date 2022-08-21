# Net Sec Challenge
Link: https://tryhackme.com/room/netsecchallenge

Practice the skills you have learned in the Network Security module.


Task 2  Challenge Questions
You can answer the following questions using Nmap, Telnet, and Hydra.

Answer the questions below
What is the highest port number being open less than 10,000?
NMAP
<br>
There is an open port outside the common 1000 ports; it is above 10,000. What is it?
NMAP<br>
How many TCP ports are open?
NMAP<br>
What is the flag hidden in the HTTP server header?
NMAP<br>
What is the flag hidden in the SSH server header?
NMAP<br>
We have an FTP server listening on a nonstandard port. What is the version of the FTP server?
NMAP<br>
We learned two usernames using social engineering: eddie and quinn. What is the flag hidden in one of these two account files and accessible via FTP?<br>
    sudo hydra -l quinn -P /usr/share/wordlists/rockyou.txt ftp://10.10.34.194:10021


Browsing to http://10.10.34.194:8080 displays a small challenge that will give you a flag once you solve it. What is the flag?<br>
nmap -sN 10.10.10.10

<!-- 
Task 2  Challenge Questions
You can answer the following questions using Nmap, Telnet, and Hydra.

Answer the questions below
What is the highest port number being open less than 10,000?
8080
There is an open port outside the common 1000 ports; it is above 10,000. What is it?

10021
How many TCP ports are open?

6
What is the flag hidden in the HTTP server header?

THM{web_server_25352}
What is the flag hidden in the SSH server header?

THM{946219583339}
We have an FTP server listening on a nonstandard port. What is the version of the FTP server?

vsftpd 3.0.3
We learned two usernames using social engineering: eddie and quinn. What is the flag hidden in one of these two account files and accessible via FTP?

THM{321452667098}
Browsing to http://10.10.34.194:8080 displays a small challenge that will give you a flag once you solve it. What is the flag?

THM{f7443f99}

-->