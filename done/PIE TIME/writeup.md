Fun time learning about binaries. So here I downloaded the c and binary file to my laptop. I used WSL to get access to sum specific tools I needed. I inputed the following into WSL command line:
```
objdump -d vuln | grep "<win>\|<main>"
```
here I got the following out put:
```
    11c1:       48 8d 3d 75 01 00 00    lea    0x175(%rip),%rdi        # 133d <main>
00000000000012a7 <win>:
000000000000133d <main>:
    1387:       48 8d 35 af ff ff ff    lea    -0x51(%rip),%rsi        # 133d <main>
```
now we know the positions of the win and main, so the different between the two is:
```
0x133d - 0x12a7 = -150
```
okay so now open the webshell and we get the main address we need, for example:
```
escobara-picoctf@webshell:~$ nc rescued-float.picoctf.net 54133
Address of main: 0x58e4abf1333d
Enter the address to jump to, ex => 0x12345:
```
in python cli I did the following 
```
hex(0x58e4abf1333d - 150)
```
Then I pasted the output from python into the program and I got the flag.