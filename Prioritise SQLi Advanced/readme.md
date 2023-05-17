Prioritise
   
In this challenge you will explore some less common SQL Injection techniques.

https://tryhackme.com/room/prioritise
We have this new to-do list application, where we order our tasking based on priority! Is it really all that secure, though...?


Adding Item:
http://10.10.149.11/?success=Added%20new%20item


Sorting Items: (Vulnerable to sql)
http://10.10.149.11/?order=title

Here is the Script for python:
source: internet
[PythonScript](./script.py)

┌──(root㉿kali)-[~/temp]
└─# python3 s.py
[+] Current Flag is f
[+] Current Flag is fl
[+] Current Flag is fla
[+] Current Flag is flag
[+] Current Flag is flag{
[+] Current Flag is flag{6
[+] Current Flag is flag{65
[+] Current Flag is flag{65f
[+] Current Flag is flag{65f2
[+] Current Flag is flag{65f2f
[+] Current Flag is flag{65f2f8
[+] Current Flag is flag{65f2f8c
[+] Current Flag is flag{65f2f8cf
[+] Current Flag is flag{65f2f8cfd
[+] Current Flag is flag{65f2f8cfd5
[+] Current Flag is flag{65f2f8cfd53
[+] Current Flag is flag{65f2f8cfd53d
[+] Current Flag is flag{65f2f8cfd53d5
[+] Current Flag is flag{65f2f8cfd53d59
[+] Current Flag is flag{65f2f8cfd53d594
[+] Current Flag is flag{65f2f8cfd53d5942
[+] Current Flag is flag{65f2f8cfd53d59422
[+] Current Flag is flag{65f2f8cfd53d59422f
[+] Current Flag is flag{65f2f8cfd53d59422f3
[+] Current Flag is flag{65f2f8cfd53d59422f3d
[+] Current Flag is flag{65f2f8cfd53d59422f3d7
[+] Current Flag is flag{65f2f8cfd53d59422f3d7c
[+] Current Flag is flag{65f2f8cfd53d59422f3d7cc
[+] Current Flag is flag{65f2f8cfd53d59422f3d7cc6
[+] Current Flag is flag{65f2f8cfd53d59422f3d7cc62
[+] Current Flag is flag{65f2f8cfd53d59422f3d7cc62c
[+] Current Flag is flag{65f2f8cfd53d59422f3d7cc62cc
[+] Current Flag is flag{65f2f8cfd53d59422f3d7cc62cc8
[+] Current Flag is flag{65f2f8cfd53d59422f3d7cc62cc8f
[+] Current Flag is flag{65f2f8cfd53d59422f3d7cc62cc8fd
[+] Current Flag is flag{65f2f8cfd53d59422f3d7cc62cc8fdc
                                                              