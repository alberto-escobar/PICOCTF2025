This challenge was a bitch to do but basically what is happening is that bininst2.exe is creating and writing a file using bad arguements. In hook.js, I change the arguements used so they are proper. The arguments modified are:

- Correct filename used for CreateFileA
- number bytes bytes written in WriteFile is more than zero.

if you run

```
frida-trace -f bininst2.exe -S hook.js
```

there will be a file written called flag.txt, open it and it is base64 encoded.

```
picoCTF{fr1da_f0r_b1n_in5trum3nt4tion!_b21aef39}
```
