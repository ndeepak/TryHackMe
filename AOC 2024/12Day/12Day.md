**Advent of Cyber 2024 [Day 12] Writeup with Answers | TryHackMe Walkthrough**
**Task 18 — Web Timing Attacks: If I can't steal their money, I'll steal their joy!**
This task revolves around performing a race condition attack on a web application, specifically targeting the transfer functionality to send money from one account to another. The goal is to exploit the system by sending multiple requests in parallel and capturing the flag after successfully transferring more money than intended.

### **Steps to Solve the Task:**
**Pre-requisite:** Make sure you are connected to the VPN before starting the task.

#### **1. What is the flag value after transferring over $2000 from Glitch's account?**
To start the attack, follow these steps:
1. **Open the web application**: Navigate to the provided URL:
    `http://MACHIN_IP:5000`
    
2. **Login** using the following credentials:
    - **Account Number:** 101
    - **Password:** glitch
3. **Initiate the transfer**:
    - Enter **111** as the account number.
    - Enter **500** as the transfer amount.
    - **Send** the transaction.
4. **Capture the POST request**: Open the **Developer Tools** (press `F12` or right-click on the page and select "Inspect") and navigate to the **Network** tab. Find the **POST /transfer** request.
    
5. **Send the request to Repeater**:
    
    - Right-click on the captured request and select **Send to Repeater**.
    - In the **Repeater tab**, **send the request 10 times** by clicking the **Send** button repeatedly.
6. **Create a request group**:
    
    - Click on the **Request tab** and then click **Create Tab Group**.
    - Select the 10 requests you just sent.
7. **Send all requests in parallel**:
    
    - Once the requests are grouped, select the option to **Send group in parallel**. This will send all 10 requests at the same time, exploiting the race condition.
8. **Get the flag**: After sending the requests, navigate to the **/dashboard** or **refresh the page** to capture the flag.
    

**Answer:**
`THM{WON_THE_RACE_007}`

---

### **Summary of Steps:**
1. Open the web app and login using the credentials.
2. Initiate a transfer and capture the POST request.
3. Use the Repeater to send the transfer request 10 times.
4. Group the requests and send them in parallel to exploit the race condition.
5. Navigate to the dashboard or refresh the page to reveal the flag.

This task demonstrates a **race condition attack**, where multiple parallel requests are sent to exploit the system and transfer more money than intended, ultimately revealing the flag.