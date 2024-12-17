### Task 15 — GRC Day 9: Risk Assessment and Vendor Evaluation
#### Introduction
Governance, Risk, and Compliance (GRC) are essential aspects of information security that help organizations ensure their practices align with legal and regulatory obligations. GRC focuses on three key areas:

1. **Governance**: Creating and implementing an organization's security strategy, policies, standards, and roles.
2. **Risk**: Identifying, assessing, and mitigating risks to IT assets.
3. **Compliance**: Ensuring adherence to legal and regulatory standards (e.g., GDPR, NIST, ISO 27001).

Effective GRC ensures that risks are quantified based on their **likelihood** and **impact**, helping to prioritize actions that minimize security breaches. In this scenario, you will assess vendors based on these criteria.

### **Risk Assessment Process**

#### Identifying Risks

- **Data at Rest/Transit Encryption**: Unencrypted data is a critical risk to data confidentiality and integrity.
- **Access Control**: Weak or poorly enforced access control can lead to unauthorized data access.
- **Data Retention**: Storing client data for too long increases the risk of unauthorized access or data breaches.

#### Assigning Likelihood and Impact

- **Likelihood**: The probability of the risk materializing (e.g., "Very Likely," "Unlikely").
- **Impact**: The potential damage or harm if the risk materializes (e.g., "Critical," "High").

#### Risk Scores

Risk scores are calculated by multiplying the **likelihood** of a risk by its **impact**. A simple scale could be:

- **1 (Low)** to **5 (Critical)** for both likelihood and impact.
- Risk = Likelihood × Impact (where each is rated from 1 to 5).

Let's now assess the vendors based on these parameters.

---

### **Vendor 1 Risk Assessment**

1. **Data Encryption**:
    
    - **AES-256** for data in transit.
    - **None** for data at rest.
    - **Impact**: Critical (data at rest is unencrypted).
    - **Likelihood**: Very Likely (encryption is typically required but not implemented for data at rest).
2. **Access Control**:
    
    - **Data can be accessed by all people in the organization**.
    - **Impact**: Critical (lack of proper access control).
    - **Likelihood**: Very Likely (pervasive access controls are often missing).
3. **Data Retention**:
    
    - **2 weeks to 1 month**.
    - **Impact**: Critical (excessive retention can lead to risks).
    - **Likelihood**: Likely (could increase over time).

#### **Risk Scores for Vendor 1**

- **Data Encryption**: 5 (Critical) × 5 (Very Likely) = **25**
- **Access Control**: 5 (Critical) × 5 (Very Likely) = **25**
- **Data Retention**: 5 (Critical) × 4 (Likely) = **20**

#### **Total Risk Score**: **70**

---

### **Vendor 2 Risk Assessment**

1. **Data Encryption**:
    
    - **None** for both data in transit and data at rest.
    - **Impact**: High (unencrypted data is highly vulnerable).
    - **Likelihood**: Very Likely (common in vendors who lack security focus).
2. **Access Control**:
    
    - **Data can be accessed only on a need-to-know basis**.
    - **Impact**: Critical (good practice but could still be a vulnerability).
    - **Likelihood**: Unlikely (access control is better implemented).
3. **Data Retention**:
    
    - **1 week to 2 weeks**.
    - **Impact**: Critical (data retention could still be a concern).
    - **Likelihood**: Possible (a reasonable duration).

#### **Risk Scores for Vendor 2**

- **Data Encryption**: 4 (High) × 5 (Very Likely) = **20**
- **Access Control**: 5 (Critical) × 3 (Unlikely) = **15**
- **Data Retention**: 5 (Critical) × 3 (Possible) = **15**

#### **Total Risk Score**: **50**

---

### **Vendor 3 Risk Assessment**

1. **Data Encryption**:
    
    - **None** for both data in transit and data at rest.
    - **Impact**: High.
    - **Likelihood**: Very Likely.
2. **Access Control**:
    
    - **Data can be accessed only on a need-to-know basis**.
    - **Impact**: Critical.
    - **Likelihood**: Unlikely.
3. **Data Retention**:
    
    - **More than 1 month**.
    - **Impact**: Critical.
    - **Likelihood**: Very Likely.

#### **Risk Scores for Vendor 3**

- **Data Encryption**: 4 (High) × 5 (Very Likely) = **20**
- **Access Control**: 5 (Critical) × 3 (Unlikely) = **15**
- **Data Retention**: 5 (Critical) × 5 (Very Likely) = **25**

#### **Total Risk Score**: **60**

---

### **Risk Evaluation and Vendor Selection**

- **Vendor 1**: **70** (High risk due to lack of encryption and weak access control).
- **Vendor 2**: **50** (Moderate risk with issues in encryption and data retention).
- **Vendor 3**: **60** (High risk due to poor encryption and lengthy data retention).

#### **Recommendation**:

Based on the calculated risk scores, **Vendor 2** has the lowest overall risk and is the most secure option to choose, though the vendor should improve encryption for both data in transit and at rest, as well as manage retention better.