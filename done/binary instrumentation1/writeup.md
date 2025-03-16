did tracing so I suspected they used a sleep function so I traced for that using

```
frida-trace -f bininst1.exe -i "Sleep"
```

the above opens frida-trace, hooks on APIS called "Sleep", and then spawns the file. you will see an output like this

```
Started tracing 2 functions. Web UI available at http://localhost:60632/
Hi, I have the flag for you just right here!
I'll just take a quick nap before I print it out for you, should only take me a decade or so!
zzzzzzzz....
           /* TID 0x1e28 */
    12 ms  Sleep()
    12 ms     | Sleep()
```

all this confirms is that the program uses sleep. So now we want to overwrite sleep somehow. So I made the `hook.js` file. This alters any values made to `Sleep` to be 1 to redeuce the sleep time. I then called the file using:

```
frida-trace -f bininst1.exe -S hook.js
```

the flag will print

picoCTF{w4ke_m3_up_w1th_fr1da_f27acc38}
