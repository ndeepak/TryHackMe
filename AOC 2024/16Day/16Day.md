**Advent of Cyber 2024 [Day 16] Writeup with Answers | TryHackMe Walkthrough**
**Task 22 — Azure: The Wareville's Key Vault grew three sizes that day.**
In this task, we explore Azure-related services, focusing on the **Azure Key Vault**, **Azure Active Directory**, and how to retrieve and manipulate secrets stored in Azure. These are critical components in cloud environments to ensure secure access and storage of sensitive information.

---

### **Steps to Solve the Task:**

#### **1. What is the password for backupware that was leaked?**
**Instructions:**
1. Use the Azure CLI command to list all users in Azure Active Directory (AD) and look for **backupware** and their office location.
    `az ad user list`
    
2. Identify the user **backupware** and find the leaked password.

**Answer:**
`R3c0v3r_s3cr3ts!`

---

#### **2. What is the group ID of the Secret Recovery Group?**
**Instructions:**
1. List all the groups in Azure AD using the following command:
    `az ad group list`
    
2. Identify the **group ID** associated with the **Secret Recovery Group**.

**Answer:**
`7d96660a-02e1-4112-9515-1762d0cb66b7`

---

#### **3. What is the name of the vault secret?**

**Instructions:**

1. Use the following command to list all the Key Vaults:
    `az keyvault list`
    
2. Identify the **vault name** and use it to list the secrets in the vault:
    `az keyvault secret list --vault-name warevillesecrets`
    

**Answer:**
`aoc2024`

---

#### **4. What are the contents of the secret stored in the vault?**

**Instructions:**

1. Use the following command to view the contents of the secret:
    `az keyvault secret show --vault-name warevillesecrets --name aoc2024`
    

**Answer:**
`WhereIsMyMind1999`

---

### **Summary of Steps:**
1. Use the **Azure CLI** to list all users and find the leaked password for **backupware**.
2. List all Azure AD groups to find the **group ID** of the **Secret Recovery Group**.
3. List the **Key Vault secrets** and identify the **name of the vault secret**.
4. Retrieve and display the **contents of the secret** stored in the Azure Key Vault.

This task highlights how to interact with **Azure Key Vault** and **Azure Active Directory (Entra ID)** to retrieve secrets and group information, which are essential for cloud-based security and management.