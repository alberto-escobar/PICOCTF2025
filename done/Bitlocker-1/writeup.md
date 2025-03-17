God this was hard to figure out. First I installed john the ripper.

then I ran `bitlocker2john -i bitlocker-1.dd > cat hash.txt` to get the hash of the bitlocker

thius extracts the hash so I can brute force it with hash cat, which i did with this command: `hashcat -m 22100 backup.txt example.dict`

after 20 mins, the password is `jacquelin`

last step is to decrypt the drive and access the files this is done by:

```
mkdir /mnt/bitlocker /mnt/decrypt
dislocker -V bitlocker-1.dd -u -- /mnt/bitlocker
YOU WILL BE PROMPTED WITH THE PASSWORD
sudo mount -o loop /mnt/bitlocker/dislocker-file /mnt/decrypted
cd /mnt/decrypted
nano flag.txt
```

tada!

```
picoCTF{us3_b3tt3r_p4ssw0rd5_pl5!_3242adb1}
```
