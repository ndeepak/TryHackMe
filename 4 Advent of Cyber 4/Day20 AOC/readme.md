Title
firmwareREv8
IP Address
10.10.14.161

Tools used:
BinWalk: extracts code snippets
Firmware ModKit (FMK) : used for firmware reverse engineering, outputs a dir with firmware file system.
FirmWalker: not used 



Last login: Wed Dec 21 06:48:32 2022 from 10.100.1.176
test@ip-10-10-73-87:~$ dir
bin  bin-unsigned  firmware-mod-kit
test@ip-10-10-73-87:~$ ls
bin  bin-unsigned  firmware-mod-kit
test@ip-10-10-73-87:~$ 

# Step 1: Verifying Encryption

test@ip-10-10-73-87:~$ cd bin
test@ip-10-10-73-87:~/bin$ ls
firmwarev2.2-encrypted.gpg
test@ip-10-10-73-87:~/bin$ binwalk -E -N firmwarev2.2-encrypted.gpg 

DECIMAL       HEXADECIMAL     ENTROPY
------------------------------------------------------------------------------
--
0             0x0             Rising entropy edge (0.989903)

In the above output, the rising entropy edge means that the file is probably encrypted and has increased randomness. 

# Step 2: Finding Unencrypted Older Version

test@ip-10-10-73-87:~/bin$ cd
test@ip-10-10-73-87:~$ ls
bin  bin-unsigned  firmware-mod-kit
test@ip-10-10-73-87:~$ cd bin-unsigned/
test@ip-10-10-73-87:~/bin-unsigned$ ls
firmwarev1.0-unsigned
test@ip-10-10-73-87:~/bin-unsigned$ 

test@ip-10-10-73-87:~/bin-unsigned$ extract-firmware.sh firmwarev1.0-unsigned 
Firmware Mod Kit (extract) 0.99, (c)2011-2013 Craig Heffner, Jeremy Collake

Scanning firmware...

Scan Time:     2022-12-21 06:55:38
Target File:   /home/test/bin-unsigned/firmwarev1.0-unsigned
MD5 Checksum:  b141dc2678be3a20d4214b93354fedc0
Signatures:    344

DECIMAL       HEXADECIMAL     DESCRIPTION
------------------------------------------------------------------------------
--
0             0x0             TP-Link firmware header, firmware version: 0.-15
360.3, image version: "", product ID: 0x0, product version: 138412034, kernel 
load address: 0x0, kernel entry point: 0x80002000, kernel offset: 4063744, ker
nel length: 512, rootfs offset: 849104, rootfs length: 1048576, bootloader off
set: 2883584, bootloader length: 0
13344         0x3420          U-Boot version string, "U-Boot 1.1.4 (Apr  6 201
6 - 11:12:23)"
13392         0x3450          CRC32 polynomial table, big endian
14704         0x3970          uImage header, header size: 64 bytes, header CRC
: 0x5A946B00, created: 2016-04-06 03:12:24, image size: 35920 bytes, Data Addr
ess: 0x80010000, Entry Point: 0x80010000, data CRC: 0x510235FE, OS: Linux, CPU
: MIPS, image type: Firmware Image, compression type: lzma, image name: "u-boo
t image"
14768         0x39B0          LZMA compressed data, properties: 0x5D, dictiona
ry size: 33554432 bytes, uncompressed size: 93944 bytes
131584        0x20200         TP-Link firmware header, firmware version: 0.0.3
, image version: "", product ID: 0x0, product version: 138412034, kernel load 
address: 0x0, kernel entry point: 0x80002000, kernel offset: 3932160, kernel l
ength: 512, rootfs offset: 849104, rootfs length: 1048576, bootloader offset: 
2883584, bootloader length: 0
132096        0x20400         LZMA compressed data, properties: 0x5D, dictiona
ry size: 33554432 bytes, uncompressed size: 2494744 bytes
1180160       0x120200        Squashfs filesystem, little endian, version 4.0,
 compression:lzma, size: 2812026 bytes, 600 inodes, blocksize: 131072 bytes, c
reated: 2022-11-17 11:14:32

Extracting 1180160 bytes of tp-link header image at offset 0
Extracting squashfs file system at offset 1180160
3994112
3994112
0
Extracting squashfs files...
[sudo] password for test: 
Firmware extraction successful!
Firmware parts can be found in '/home/test/bin-unsigned/fmk/*'
test@ip-10-10-73-87:~/bin-unsigned$ 


# Step 3: Finding Encryption Keys

find a public, and private key and a paraphrase to decrypt the originally signed firmware. 

--
test@ip-10-10-73-87:~/bin-unsigned$ grep -ir key
Binary file firmwarev1.0-unsigned matches
Binary file fmk/image_parts/rootfs.img matches
Binary file fmk/rootfs/usr/sbin/dropbearmulti matches
................................
............................
key").style.display=(wlanFilterAdvPara[9])?"block":"none";
fmk/rootfs/gpg/public.key:-----BEGIN PGP PUBLIC KEY BLOCK-----
fmk/rootfs/gpg/public.key:-----END PGP PUBLIC KEY BLOCK-----
fmk/rootfs/gpg/private.key:-----BEGIN PGP PRIVATE KEY BLOCK-----
fmk/rootfs/gpg/private.key:-----END PGP PRIVATE KEY BLOCK-----
test@ip-10-10-73-87:~/bin-unsigned$ grep -ir paraphrase
fmk/rootfs/gpg/secret.txt:PARAPHRASE: Santa@2022
test@ip-10-10-73-87:~/bin-unsigned$ 

# Step 4: Decrypting the Encrypted Firmware

test@ip-10-10-73-87:~/bin-unsigned$ gpg --import fmk/rootfs/gpg/private.key 
gpg: key 56013838A8C14EC1: "McSkidy <mcskidy@santagift.shop>" not changed
gpg: key 56013838A8C14EC1: secret key imported
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg:       secret keys read: 1
gpg:  secret keys unchanged: 1
test@ip-10-10-73-87:~/bin-unsigned$ 

test@ip-10-10-73-87:~/bin-unsigned$ gpg --import fmk/rootfs/gpg/public.key 
gpg: key 56013838A8C14EC1: "McSkidy <mcskidy@santagift.shop>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
test@ip-10-10-73-87:~/bin-unsigned$ 

test@ip-10-10-73-87:~/bin-unsigned$ gpg --list-secret-keys
/home/test/.gnupg/pubring.kbx 
sec   rsa3072 2022-11-17 [SC] [expires: 2024-11-16]
      514B4994E9B3E47A4F89507A56013838A8C14EC1
uid           [ unknown] McSkidy <mcskidy@santagift.shop>
ssb   rsa3072 2022-11-17 [E] [expires: 2024-11-16]

test@ip-10-10-73-87:~/bin-unsigned$ 

$  gpg firmwarev2.2-encrypted.gpg
Use the paraphrase
gpg: encrypted with 3072-bit RSA key, ID 1A2D5BB2F7076FA8, created 2022-11-17
      "McSkidy <mcskidy@santagift.shop>"
test@ip-10-10-73-87:~/bin$ ls
firmwarev2.2-encrypted  firmwarev2.2-encrypted.gpg
test@ip-10-10-73-87:~/bin$ 

# Step 5: Reversing the Original Encrypted Firmware

test@ip-10-10-73-87:~/bin$ extract-firmware.sh firmwarev2.2-encrypted
Firmware Mod Kit (extract) 0.99, (c)2011-2013 Craig Heffner, Jeremy Collake

Scanning firmware...

Scan Time:     2022-12-21 07:09:03
Target File:   /home/test/bin/firmwarev2.2-encrypted
MD5 Checksum:  714c30af5db1e156e35b374f87c59d6f
Signatures:    344

DECIMAL       HEXADECIMAL     DESCRIPTION
------------------------------------------------------------------------------
--
0             0x0             TP-Link firmware header, firmware version: 0.-15
360.3, image version: "", product ID: 0x0, product version: 138412034, kernel 
load address: 0x0, kernel entry point: 0x80002000, kernel offset: 4063744, ker
nel length: 512, rootfs offset: 849104, rootfs length: 1048576, bootloader off
set: 2883584, bootloader length: 0
13344         0x3420          U-Boot version string, "U-Boot 1.1.4 (Apr  6 201
6 - 11:12:23)"
13392         0x3450          CRC32 polynomial table, big endian
14704         0x3970          uImage header, header size: 64 bytes, header CRC
: 0x5A946B00, created: 2016-04-06 03:12:24, image size: 35920 bytes, Data Addr
ess: 0x80010000, Entry Point: 0x80010000, data CRC: 0x510235FE, OS: Linux, CPU
: MIPS, image type: Firmware Image, compression type: lzma, image name: "u-boo
t image"
14768         0x39B0          LZMA compressed data, properties: 0x5D, dictiona
ry size: 33554432 bytes, uncompressed size: 93944 bytes
131584        0x20200         TP-Link firmware header, firmware version: 0.0.3
, image version: "", product ID: 0x0, product version: 138412034, kernel load 
address: 0x0, kernel entry point: 0x80002000, kernel offset: 3932160, kernel l
ength: 512, rootfs offset: 849104, rootfs length: 1048576, bootloader offset: 
2883584, bootloader length: 0
132096        0x20400         LZMA compressed data, properties: 0x5D, dictiona
ry size: 33554432 bytes, uncompressed size: 2494744 bytes
1180160       0x120200        Squashfs filesystem, little endian, version 4.0,
 compression:lzma, size: 2809007 bytes, 605 inodes, blocksize: 131072 bytes, c
reated: 2022-12-01 05:42:58

Extracting 1180160 bytes of tp-link header image at offset 0
Extracting squashfs file system at offset 1180160
3990016
3990016
0
Extracting squashfs files...
Firmware extraction successful!
Firmware parts can be found in '/home/test/bin/fmk/*'
test@ip-10-10-73-87:~/bin$ 

test@ip-10-10-73-87:~$ cat bin/fmk/rootfs/flag.txt
THM{WE_GOT_THE_FIRMWARE_CODE}
test@ip-10-10-73-87:~$ 

ls -lah *