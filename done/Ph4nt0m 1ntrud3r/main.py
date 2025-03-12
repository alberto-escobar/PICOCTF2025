from scapy.all import rdpcap, Raw
import base64

pkts = rdpcap('myNetworkTraffic.pcap')


pkts = sorted(pkts, key=lambda p: p.time)
flag = ""
for i, p in enumerate(pkts, start=1):
    try:
        print(f'no={i}, t={p.time}, load={base64.decodebytes(p[Raw].load).decode("ascii")}')
        flag += base64.decodebytes(p[Raw].load).decode("ascii")
    except:
        continue

print(flag)