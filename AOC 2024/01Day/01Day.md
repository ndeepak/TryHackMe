## **Advent of Cyber 2024 - Day 1 Writeup**

**Title:** _Maybe SOC-mas music, he thought, doesn't come from a store?_

**Description:**  
McSkidy found a suspicious website that claimed to convert videos to mp3 files. However, something seemed off, and McSkidy discovered a malicious intent behind the scenes. The investigation led to uncovering an OPSEC mistake and tracking down "The Glitch."

---

### **Task 7: Maybe SOC-mas music, he thought, doesn't come from a store?**

1. **Question 1:** _Looks like the song.mp3 file is not what we expected! Run `exiftool song.mp3` in your terminal to find out the author of the song. Who is the author?_
    
    - **Approach:**  
        Use the `exiftool` command to extract metadata from the `song.mp3` file.
        `exiftool song.mp3`
        
    - **Answer:** Tyler Ramsbey

---

2. **Question 2:** _The malicious PowerShell script sends stolen info to a C2 server. What is the URL of this C2 server?_
    
    - **Approach:**
        
        - Run `exiftool` on the file again to identify any hidden URLs.
        - A URL pointing to a PowerShell script was found:  
            **`https://raw.githubusercontent.com/MM-WarevilleTHM/IS/refs/heads/main/IS.ps1`**
        - Inspect the PowerShell script content to locate the C2 server URL.
    - **C2 Server URL:**
        `http://papash3ll.thm/data`
        
    - **Answer:** [http://papash3ll.thm/data](http://papash3ll.thm/data)
        

---

3. **Question 3:** _Who is M.M? Maybe his GitHub profile page would provide clues?_
    
    - **Approach:**
        - Search GitHub for the phrase **"Created by the one and only M.M."**:  
            [GitHub Search Link](https://github.com/search?q=%22Created+by+the+one+and+only+M.M.%22&type=issues)
        - Explore the results to find the GitHub profile associated with M.M.
        - Inspect the repositories to determine M.M's full name.
    - **Answer:** Mayor Malware

---

4. **Question 4:** _What is the number of commits on the GitHub repo where the issue was raised?_
    
    - **Approach:**
        
        - Visit the identified GitHub repository.
        - Check the repository’s commit history to find the total number of commits.
    - **Observation:** The repository has **1 commit**.
        
    - **Answer:** 1
        

---

### **Summary of Tools and Commands Used**

1. **ExifTool**: Extracts metadata from files like images, audio, or video.
    
    - **Command:** `exiftool filename`
2. **GitHub Search**: Helps in identifying user profiles, repositories, and issues.
    
3. **PowerShell Inspection**: Analyze suspicious scripts for hidden URLs or malicious behavior.