## **Advent of Cyber 2024 - Day 7 Writeup**

**Title:** _Oh, no. I'M SPEAKING IN CLOUDTRAIL!_

---

### **Task 13 — AWS Log Analysis**

In this task, we analyze AWS CloudTrail logs using `jq` to extract meaningful data about user activities and security events.

---
### **1. What is the other activity made by the user "glitch" aside from the `ListObject` action?**
#### **Approach:**
1. Use the following `jq` command to filter CloudTrail logs for the user "glitch" and list their activities:
    `jq -r '["Event_Time", "Event_Source", "Event_Name", "User_Name", "Source_IP"],(.Records[] | select(.userIdentity.userName == "glitch") | [.eventTime, .eventSource, .eventName, .userIdentity.userName // "N/A", .sourceIPAddress // "N/A"]) | @tsv' cloudtrail_log.json | column -t -s $'\t'`
    
2. **Look for the `PutObject` event** in the output, which is the additional activity performed by the "glitch" user.
    

#### **Answer:**
`PutObject`

---

### **2. What is the source IP related to the S3 bucket activities of the user "glitch"?**

#### **Approach:**

1. Inspect the output from the previous command to find the **source IP** associated with "glitch"'s activities related to the S3 bucket.

#### **Answer:**

`53.94.201.69`

---

### **3. Based on the `eventSource` field, what AWS service generates the `ConsoleLogin` event?**

#### **Approach:**

1. Check the `eventSource` field in the `ConsoleLogin` event in the CloudTrail logs. This will tell us which service generated the event.

#### **Answer:**

`signin.amazonaws.com`

---

### **4. When did the anomalous user trigger the `ConsoleLogin` event?**

#### **Approach:**

1. Extract the **event time** from the `ConsoleLogin` event using the information in the logs. This is the timestamp when the user triggered the login event.

#### **Answer:**

The specific time will be available in the `eventTime` field of the `ConsoleLogin` event.

---

### **5. What was the name of the user that was created by the "mcskidy" user?**

#### **Approach:**

1. Review the CloudTrail logs to find the event where "mcskidy" created a new user. The **username** will be visible in the output.

#### **Answer:**

`glitch`

---

### **6. What type of access was assigned to the anomalous user?**

#### **Approach:**

1. Filter the logs for the `AttachUserPolicy` event, which will reveal the permissions assigned to the newly created user.
    `jq '.Records[] | select(.eventSource=="iam.amazonaws.com" and .eventName== "AttachUserPolicy")' cloudtrail_log.json`
    

#### **Answer:**

`AdministratorAccess`

---

### **7. Which IP does Mayor Malware typically use to log into AWS?**

#### **Approach:**

1. The source IP for Mayor Malware's activities was found earlier in the logs.

#### **Answer:**

`53.94.201.69`

---

### **8. What is McSkidy's actual IP address?**

#### **Approach:**

1. Use the following `jq` command to filter logs for "mcskidy" and find their **source IP**:
    `jq -r '["Event_Time","Event_Source","Event_Name", "User_Name","User_Agent","Source_IP"],(.Records[] | select(.userIdentity.userName=="mcskidy") | [.eventTime, .eventSource, .eventName, .userIdentity.userName // "N/A",.userAgent // "N/A",.sourceIPAddress // "N/A"]) | @tsv' cloudtrail_log.json | column -t -s $'\t'`
    

#### **Answer:**

`31.210.15.79`

---

### **9. What is the bank account number owned by Mayor Malware?**

#### **Approach:**

1. Use the `grep` command to search the `rds.log` file for the string "Mayor" to find the bank account number.
    `grep Mayor rds.log`
    

#### **Answer:**
`2394 6912 7723 1294`

---

### **Summary of Tools and Techniques Used:**

- **`jq`**: A command-line tool for parsing JSON data, used to extract and filter specific details from CloudTrail logs.
- **`grep`**: A command-line tool to search for specific strings in text files, used here to extract information from `rds.log`.

---

### **Key Learnings:**

- **CloudTrail Logs Analysis**: How to interpret AWS CloudTrail logs to track user activities and security events.
- **Using `jq`**: Practical experience with using `jq` to parse and filter JSON data.
- **AWS IAM**: Understanding how IAM policies are attached and how to identify user activities and permissions.