## **Advent of Cyber 2024 - Day 4 Writeup**
**Title:** _I'm all atomic inside!_

---
### **Task 10 — Atomic Red Team**
---
### **1. What was the flag found in the `.txt` file that is found in the same directory as the PhishingAttachment.xslm artifact?**

#### **Approach:**

1. Run the following command to simulate the phishing attack:
    `Invoke-AtomicTest T1566.001 -TestNumbers 1`
    
2. Navigate to the **Temp directory**:
    
    - Path: `C:\Users\Administrator\AppData\Local\Temp\`
3. Locate the `.txt` file and extract the flag.
    

#### **Answer:**

`THM{GlitchTestingForSpearphishing}`

---

### **2. What ATT&CK technique ID would be our point of interest?**

#### **Approach:**

- The passage references **"command and scripting interpreter"**.
- Search for the **MITRE ATT&CK** ID associated with **command and scripting interpreter**.

#### **Answer:**

`T1059`

---

### **3. What ATT&CK subtechnique ID focuses on the Windows Command Shell?**

#### **Approach:**

- Search for the subtechnique ID related to the **Windows Command Shell** under the **T1059** technique in MITRE ATT&CK.

#### **Answer:**

`T1059.003`

---

### **4. What is the name of the Atomic Test to be simulated?**

#### **Approach:**

1. Run the following command to display details of the **Windows Command Shell** test:
    `Invoke-AtomicTest T1059.003 -ShowDetails`
    
2. Review the output to identify the name of the Atomic Test.
    

#### **Answer:**
`Simulate BlackByte Ransomware Print Bombing`

---

### **5. What is the name of the file used in the test?**

#### **Approach:**

- In the output of the `Invoke-AtomicTest` command (from the previous step), locate the filename used during the simulation.

#### **Answer:**

`Wareville_Ransomware.txt`

---

### **6. What is the flag found from this Atomic Test?**

#### **Approach:**

1. Execute the following command to run the specific test:
    `Invoke-AtomicTest T1059.003 -TestNumbers 4`
    
2. Save the output as a file or PDF to extract the flag.
    
3. Locate and read the flag from the output.
    

#### **Answer:**
`THM{R2xpdGNoIGlzIG5vdCB0aGUgZW5lbXk=}`

---

### **Summary of Tools and Techniques Used:**

1. **Tools:**
    
    - PowerShell (Atomic Red Team)
    - MITRE ATT&CK Framework
2. **Commands:**
    
    - `Invoke-AtomicTest` to simulate various techniques and retrieve outputs.
3. **Concepts:**
    
    - MITRE ATT&CK Techniques and Subtechniques
    - Simulating phishing and command execution attacks

---

### **Key Learnings:**

- **Atomic Red Team:** A framework for simulating adversarial techniques based on the MITRE ATT&CK matrix.
- **Phishing and Command Execution:** Learned how to simulate and analyze phishing attachments and command shell abuse.