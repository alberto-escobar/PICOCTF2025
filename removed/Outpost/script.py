import hashlib

cipher = "9b4116dca85145135d175fac5517f78f673d7b48c30a34a89a5f22d90e2475fc6be940f25d7c7cd0c780f228173f88952ec515fc62c2ff6dfb30abab224c1af807104339e3cb5b775abfbff6bc045861ed1dbee01c32909ddf472d4654c29227689a3e521c0b627860e783a77c021a55f1cca1e122fe2e42dae1b1b73566e1c968a4666e91f07512e22887d95d101ba3a4bd9dbbec643d91f6d008163c0b48ed71b727f2f3903d273745903a3ad99638b5171a59d756555e1833acf96c238f5ffbdc8c4aaea128e995bcf4c248a523a150b94bedcd6f2f0c046e6db95fb5402c"

cipherBytes = bytes.fromhex(cipher)

known = "Great and Noble Leader of the Ta"

knownBytes = bytes(known, "utf-8")

key = []

for i in range(len(known)):
    key.append(knownBytes[i]^cipherBytes[i])

key = bytes(key)

text = ""

for i in range(len(cipher)//2):
    text += chr(key[i%32]^cipherBytes[i])
    if i>0 and i%32 == 0:
        key = bytes.fromhex(hashlib.sha256(bytes(key)).hexdigest())

print(text)