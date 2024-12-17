## **Advent of Cyber 2024 - Day 2 Writeup**
**Title:** _One man's false positive is another man's potpourri_
**Description:**  
In this scenario, The Glitch attempts a brute-force attack, causing confusion with failed login attempts. SOC analysts must use their investigative superpowers to identify the root cause and uncover the malicious activity while ensuring the false positives are addressed properly.

---

### **Task 8: One man's false positive is another man's potpourri**

1. **Question 1:** _What is the name of the account causing all the failed login attempts?_
    - **Approach:**
        - Check the logs under the **user name** column to identify the account responsible for repeated failed login attempts.
    - **Answer:** `service_admin`

---

2. **Question 2:** _How many failed logon attempts were observed?_
    - **Approach:**
        - Set the **time frame** to between **Nov 29 00:00** and **Dec 1 09:30**.
        - Filter the logs using the `event.outcome` field to display only **failed** login attempts.
        - Count the total number of failures.
    - **Answer:** `6791`

---

3. **Question 3:** _What is the IP address of Glitch?_
    
    - **Approach:**
        - Add the `source.ip` field to the log filters.
        - Look for the IP address responsible for the failed login attempts.
    - **Answer:** `10.0.255.1`

---

4. **Question 4:** _When did Glitch successfully log on to ADM-01? Format: MMM D, YYYY HH:MM:SS.SSS_
    
    - **Approach:**
        - Remove the **`event.outcome: failure`** filter.
        - Add a filter for **`event.outcome: success`** to find the successful login event.
        - Identify the timestamp when the successful logon occurred.
    - **Answer:** `Dec 1, 2024 08:54:39.000`

---

5. **Question 5:** _What is the decoded command executed by Glitch to fix the systems of Wareville?_
    
    - **Approach:**
        - The provided command was Base64-encoded:           `SQBuAHMAdABhAGwAbAAtAFcAaQBuAGQAbwB3AHMAVQBwAGQAYQB0AGUAIAAtAEEAYwBjAGUAcAB0AEEAbABsACAALQBBAHUAdABvAFIAZQBiAG8AbwB0AA==`
            
        - Use **CyberChef** to decode the Base64 command:
            - Apply the `From Base64` recipe.
            - Apply the `Decode Text` recipe, and set the encoding to **UTF-16LE (1200)** (used by PowerShell).
        - The decoded command is revealed as:
            `Install-WindowsUpdate -AcceptAll -AutoReboot`
            
    - **Answer:** `Install-WindowsUpdate -AcceptAll -AutoReboot`

---

### **Summary of Tools and Commands Used**

1. **Log Analysis Tools:**
    
    - Filters applied to log files: `event.outcome: failure` and `event.outcome: success`.
    - Identified fields: `user name`, `source.ip`.
2. **CyberChef:**
    
    - **Recipes Used:**
        - `From Base64`
        - `Decode Text` (UTF-16LE)
3. **PowerShell Encoded Command:**
    
    - Base64 encoded PowerShell commands can be decoded to reveal their actual functionality.