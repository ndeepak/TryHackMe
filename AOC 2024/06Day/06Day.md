## **Advent of Cyber 2024 - Day 6 Writeup**
**Title:** _If I can't find a nice malware to use, I'm not going._

---
### **Task 12 — Sandboxes**

---
### **1. What is the flag displayed in the popup window after the EDR detects the malware?**
#### **Approach:**

1. **Start the EDR system** by running the following PowerShell command in the `C:\Tools` directory:
    `.\JingleBells.ps1`
    
2. **Run the malware** by navigating to `C:\Tools\Malware` and double-clicking on the `MerryChristmas.exe` file.
    
3. If the EDR system is correctly set up, a **popup window** will appear with the flag.
    
4. **Exit the EDR system** by pressing `Ctrl+C` in PowerShell.
    

#### **Answer:**
`THM{GlictchWasHere}`

---

### **2. What is the flag found in the `malstrings.txt` document after running `floss.exe`, and opening the file in a text editor?**
#### **Approach:**
1. **Navigate to the FLOSS directory**.
    
2. **Run the FLOSS tool** with the following command to extract malware strings from `MerryChristmas.exe`:
    `floss.exe C:\Tools\Malware\MerryChristmas.exe | Out-file C:\tools\malstrings.txt`
    
3. After the command completes, **open `malstrings.txt`** in a text editor (such as Notepad).
    
4. **Search** for the string `Mayor Malware` within the file. The result will contain the flag.
    

#### **Answer:**
`THM{HiddenClue}`

---

### **Summary of Tools and Techniques Used:**

1. **Tools:**
    
    - **PowerShell**: Used to start and interact with the custom EDR system.
    - **FLOSS**: A tool to analyze the strings within executable files and extract useful information.
2. **Concepts:**
    
    - **Endpoint Detection and Response (EDR)**: Learning how to detect malware through EDR alerts.
    - **Malware Analysis**: Using FLOSS to extract and analyze strings from malware executables.

---

### **Key Learnings:**
- **EDR Popups**: How EDR systems detect and alert based on suspicious malware activities.
- **FLOSS Utility**: How to extract and analyze strings from malware files to uncover hidden clues.

