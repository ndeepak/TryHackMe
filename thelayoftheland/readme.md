The Lay of the Land

Link: https://tryhackme.com/room/thelayoftheland
* Network infrastrucutre
* Active Directory Environment
* Users and Groups
* Host-based security solutions
* Network-based security solutions
* Applications and services

## Task 4
C:\Users\kkidd>systeminfo | findstr Domain
OS Configuration:          Primary Domain Controller
Domain:                    *******.com


## Task 5
PS C:\Users\kkidd> Get-ADUser -Filter * -SearchBase "OU=THM,DC=thmredteam,DC=com"    

## Task 5
* PS C:\Users\thm> Get-NetFirewallProfile | Format-Table Name, Enabled
* Get-MpThreat
* PS C:\Users\kkidd> Get-NetFirewallRule | findstr "THM-Connection"         