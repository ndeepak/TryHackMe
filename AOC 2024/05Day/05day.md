## **Advent of Cyber 2024 - Day 5 Writeup**
**Title:** _SOC-mas XX-what-ee?_
**Description:**  
On Day 5 of Advent of Cyber, McSkidy faced an **XXE (XML External Entity)** injection vulnerability in a web application. The goal was to exploit the vulnerability to uncover flags hidden in different parts of the system.

---
### **Task 11: XXE Day 5 – SOC-mas XX-what-ee?**
---

### **1. What is the flag discovered after navigating through the wishes?**
#### **Approach:**
1. **Access the Product Page:**
    - Connect to TryHackMe VPN and access the provided machine IP.
2. **Intercept the Request:**
    
    - Use a proxy tool like **Burp Suite**.
    - Add a product to the wishlist and intercept the HTTP request.
3. **Inject XML Code (XXE Payload):**
    
    - Modify the intercepted request to include the following XXE payload:
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
<!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<product>
  <id>&xxe;</id>
</product>
```
        
4. **Automate the Request with Intruder:**
    
    - Send the request to **Intruder** in Burp Suite.
    - Use the **Payloads tab** to automate the testing of text document IDs:
        - **Payload Type:** Numbers
        - **Range:** 0–20
5. **Analyze Responses:**
    
    - Look for changes in the response size or status code to identify the correct document.
6. **Retrieve the Flag:**
    
    - The flag appears when the correct ID matches.

#### **Answer:**
`THM{Brut3f0rc1n6_mY_w4y}`

---

### **2. What is the flag seen on the possible proof of sabotage?**
#### **Approach:**
1. **Navigate to the Changelog URL:**
    - Access the following URL to check for clues or flags:
        `http://<machine_ip>/CHANGELOG`
        
2. **Retrieve the Flag:**
    - The flag is visible in the changelog as proof of sabotage.

#### **Answer:**
`THM{m4y0r_m4lw4r3_b4ckd00rs}`

---

### **Summary of Tools and Methods Used:**
1. **Tools:**
    - **Burp Suite:** Proxy, Repeater, and Intruder for request interception and automation.
    - **TryHackMe VPN:** To access the machine IP securely.
2. **Techniques:**
    
    - **XXE Injection:** Exploited XML parsing vulnerability to extract sensitive files.
    - **Automation with Intruder:** Used Burp Suite Intruder to brute-force document IDs.
    - **URL Inspection:** Directly accessed the `/CHANGELOG` file for sabotage clues.

---

### **Key Concepts Learned:**

1. **XXE Injection:**
    
    - A type of attack that exploits vulnerabilities in XML parsers to access files or execute commands on a server.
2. **Automating Requests:**
    
    - Using tools like Burp Suite's Intruder to quickly test multiple payloads and analyze responses.