**Advent of Cyber 2024 [Day 14] Writeup with Answers | TryHackMe Walkthrough**
**Task 20 — Certificate Mismanagement: Even if we're horribly mismanaged, there'll be no sad faces on SOC-mas!**
In this task, you'll explore certificate mismanagement, gain knowledge of certificate details, and exploit them to obtain flags. You’ll also work with Burp Suite to intercept and analyze HTTP traffic.

---

### **Steps to Solve the Task:**
#### **1. What is the name of the CA that has signed the Gift Scheduler certificate?**
**Instructions:**
1. **Start the Attackbox** and navigate to it.
    
2. Add the following command to your `/etc/hosts` file to ensure that your system resolves the **gift-scheduler.thm** domain correctly:
    `echo "MACHINE_IP gift-scheduler.thm" >> /etc/hosts`
    
3. Open **gift-scheduler.thm** in your browser.
    
4. When you see the security warning about the website’s certificate, click on **"Advanced"** to expand the details.
    
5. Click on **"View certificate"** to see the full details of the certificate.
    
6. **Find the name of the Certificate Authority (CA)** that signed the certificate in the certificate details.
    

**Answer:**
`THM`

---

#### **2. What is the password for the snowballelf account?**
**Instructions:**
1. Open **Burp Suite** and configure it to proxy traffic from your browser.
    
2. In Burp Suite, navigate to the **Proxy** tab. Make sure to turn off **Intercept** so the requests are not delayed for the user.
    
3. Set up a new **listener** on your AttackBox IP address in the **Proxy settings**.
    
4. In the **HTTP history tab** under Proxy, inspect the requests that are being sent from the browser.
    
5. Look for the **POST requests** in the HTTP history. Find the request that contains the password for the **snowballelf** account.
    

**Answer:**
`c4rrotn0s3`

---

#### **3. Use the credentials for any of the elves to authenticate to the Gift Scheduler website. What is the flag shown on the elves' scheduling page?**
**Instructions:**
1. Use the **snowballelf account credentials** (`c4rrotn0s3`) to log in to the **Gift Scheduler** website.
    
2. After logging in, navigate to the **scheduling page** where the flag is displayed.
    

**Answer:**
`THM{AoC-3lf0nth3Sh3lf}`

---

#### **4. What is the password for Marta May Ware's account?**

**Instructions:**

1. Check out the **requests** in Burp Suite for any information related to Marta May Ware's account.
    
2. Look for the password in the intercepted requests related to Marta’s account.
    

**Answer:**
`H0llyJ0llySOCMAS!`

---

#### **5. Mayor Malware finally succeeded in his evil intent: with Marta May Ware's username and password, he can finally access the administrative console for the Gift Scheduler. G-Day is cancelled! What is the flag shown on the admin page?**
**Instructions:**
1. **Login to Marta’s account** with the credentials (`H0llyJ0llySOCMAS!`).
    
2. After logging in to the admin console, check for the flag displayed on the page.
    

**Answer:**
`THM{AoC-h0wt0ru1nG1ftD4y}`

---

### **Summary of Steps:**

1. **Find the CA that signed the certificate** by examining the certificate details in the browser.
2. Use **Burp Suite** to intercept and inspect HTTP traffic to find credentials for the snowballelf account.
3. **Login using the snowballelf credentials** and retrieve the flag from the elves' scheduling page.
4. Find the **password for Marta May Ware's account** in the intercepted requests.
5. **Login to the admin console using Marta’s credentials** and retrieve the flag from the admin page.

This task involves a combination of analyzing certificates, intercepting HTTP traffic, and exploiting mismanagement of credentials and access control to retrieve flags.