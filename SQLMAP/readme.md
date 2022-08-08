# SQLMAP
by Naresh Lamgade

https://tryhackme.com/room/sqlmap

Try to Answer it by yourself or See RAW for hints

Which flag or option will allow you to add a URL to the command?
<!-- -u -->



Which flag would you use to add data to a POST request?
<!-- --data -->


There are two parameters: username and password. How would you tell sqlmap to use the username parameter for the attack?
<!-- -p username -->


Which flag would you use to show the advanced help menu?
<!-- -hh -->



Which flag allows you to retrieve everything?
<!-- -a -->



Which flag allows you to select the database name?
<!-- -D -->



Which flag would you use to retrieve database tables?
<!-- --tables -->

Which flag allows you to retrieve a table’s columns?
<!-- --columns -->

Which flag allows you to dump all the database table entries?
<!-- --dump-all -->

Which flag will give you an interactive SQL Shell prompt?
<!-- --sql-shell -->

You know the current db type is 'MYSQL'. Which flag allows you to enumerate only MySQL databases?
<!-- --dbms=mysql -->


## Gobuster

```
root@ip-10-10-37-191:~# gobuster dir -u 10.10.226.224 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.226.224
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/08/08 13:45:52 Starting gobuster
===============================================================
```
HERE DIRECTORY
<!-- /blood (Status: 301) -->

```
What is the name of the interesting directory ?
loo
Who is the current db user? 
ro
What is the final flag? 
<!--  -->
```
<!-- thm{sqlm@p_is_L0ve} -->