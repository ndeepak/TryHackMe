**Advent of Cyber 2024 [Day 13] Writeup with Answers | TryHackMe Walkthrough**
**Task 19 — WebSockets: It came without buffering! It came without lag!**
In this task, you'll be working with **WebSockets**, which allow for interactive communication between the user's browser and the server in real time. You will capture and modify WebSocket messages to extract flags.

---
### **Steps to Solve the Task:**
#### **1. What is the value of Flag1?**
**Instructions:**
1. **Open the Machine IP** in a new tab.
    
2. **Click "Track"** to begin tracking the user activity. You will then need to capture the WebSocket message that corresponds to the user tracking.
    
3. In your browser's **Developer Tools**, go to the **Network** tab and **filter for WebSocket** traffic. Look for a WebSocket request that contains the following:
    `42["track", {"userId": "5"}]`
    
4. **Modify the user ID** in the WebSocket message from `5` to `6`, `7`, or `8`. The goal is to change the user ID to track a different user.
    
5. **Send the modified WebSocket request** and look for the flag. Once the modified message is sent, you should receive Flag1.
    

**Answer:**
`THM{dude_where_is_my_car}`

---

#### **2. What is the value of Flag2?**

**Instructions:**

1. **Type a message** in the WebSocket interface and capture the request in the **Network** tab.
    
2. **Look for the WebSocket message** that contains the message you're sending. It will be something like:
    `42["message", {"userId": "X", "message": "Your message"}]`
    
    (where `X` is the user ID and "Your message" is the text you've sent).
    
3. **Change the user ID** in the message to `8` (or `6` or `7`), but the key here is to replace the user ID with the "Mayor Malware". This allows you to impersonate this user.
    
4. **Send the modified message** and look for the second flag.
    

**Answer:**
`THM{my_name_is_malware._mayor_malware}`

---

### **Summary of Steps:**

1. For Flag1, capture the WebSocket request that tracks the user with `userId: 5`, modify the ID, and capture the flag.
2. For Flag2, capture the WebSocket message when you send a message, modify the user ID to `8` (or another valid ID like `6` or `7`), and impersonate the "Mayor Malware" user to retrieve the flag.

By modifying the WebSocket traffic in real-time, you were able to manipulate the data and extract the flags. This task helps illustrate how WebSocket communication can be intercepted and modified to achieve different outcomes in a web application.