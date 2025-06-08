**Advent of Cyber 2024 [Day 15] Writeup with Answers | TryHackMe Walkthrough**

**Task 21 — Active Directory: Be it ever so heinous, there's no place like Domain Controller.**

This task focuses on investigating logs, PowerShell history, and Group Policy Objects (GPOs) to gather information about a user, Glitch_Malware, and identify persistence mechanisms used in an Active Directory environment.

---

### **Steps to Solve the Task:**

#### **1. On what day was Glitch_Malware last logged in?**

**Instructions:**

1. Open **Event Viewer** on the target machine.
2. Navigate to **Windows Logs > Security**.
3. Use the **Find** option and search for the keyword **"Glitch_Malware"** in the logs.
4. Look for the last login entry for the **Glitch_Malware** user to determine the date.

**Answer:**
`07/11/2024`

---

#### **2. What event ID shows the login of the Glitch_Malware user?**

**Instructions:**

1. In **Event Viewer**, find the event associated with **Glitch_Malware's login**.
2. Check the **Task Category**, which should indicate that it is a **login** event.
3. Identify the **Event ID** related to this login.

**Answer:**
`4624`

---

#### **3. Read the PowerShell history of the Administrator account. What was the command that was used to enumerate Active Directory users?**

**Instructions:**

1. Open **File Explorer** and paste the following path in the address bar:
`C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt`
    
2. Check the first few lines of the **ConsoleHost_history.txt** file to find the command used by the Administrator account to enumerate Active Directory users.

**Answer:**
`Get-ADUser -Filter * -Properties MemberOf | Select-Object Name`

---

#### **4. Look in the PowerShell log file located in Application and Services Logs -> Windows PowerShell. What was Glitch_Malware's set password?**

**Instructions:**

1. In **Event Viewer**, navigate to **Application and Services Logs > Microsoft > Windows > PowerShell**.
2. Search for **$password** in the log entries to find the password set by **Glitch_Malware**.

**Answer:**
`SuperSecretP@ssw0rd!`

---

#### **5. Review the Group Policy Objects present on the machine. What is the name of the installed GPO?**

**Instructions:**

1. Open **PowerShell** on the machine.
2. Run the following command to list all Group Policy Objects (GPOs) installed on the system:
    `get-gpo -all`
    
3. Look for a GPO related to **Glitch_Malware** persistence.

**Answer:**
`Malicious GPO - Glitch_Malware Persistence`

---

### **Summary of Steps:**

1. Use **Event Viewer** to find the **last login date** for the **Glitch_Malware** user.
2. Identify the **Event ID** associated with **Glitch_Malware's login**.
3. Review the **PowerShell history** to find the command used to **enumerate Active Directory users**.
4. Inspect the **PowerShell logs** for the **set password** for **Glitch_Malware**.
5. Use **PowerShell** to check for any installed **Group Policy Objects** related to **Glitch_Malware's persistence**.

This task revolves around Active Directory investigation techniques, including reviewing logs, PowerShell commands, and GPOs to trace malicious activity and persistence mechanisms.