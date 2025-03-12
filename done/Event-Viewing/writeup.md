This flag is split into 3 parts and is hidden in 3 events in the event log. 

look for 3 events, two of which you should find by finding the string `Totally_Legit_Software` and the last event is of id 1074 that has a base64 comment. 
the events are:
1. 11707 software installation
2.  4657 registry modification
3.  1074 shutdown

My flags was parted like this:

```
picoCTF{Ev3nt_vi3wv3r_

1s_a_pr3tty_us3ful_

t00l_81ba3fe9}
```

all parts of the flag were in base64 encoding.