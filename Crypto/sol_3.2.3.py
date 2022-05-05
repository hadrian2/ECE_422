import urllib.request, urllib.error, urllib.parse
import sys
def main(in_hex,out_plain):
    with open(in_hex) as f:
        inHex = f.read().strip()
    Plaintext = ''
    for i in range(int((len(inHex)/32)-1)):

        Plaintext += solve_block(inHex[i*32:i*32+32],inHex[i*32+32:i*32+64])
        print(Plaintext)
    with open(out_plain,'w') as o:
        o.write(Plaintext)


def solve_block(intermediate,ciphertext):
    PadScheme = pad('')
    inter_tmp = intermediate
    PreXorMessage = []

    for j in reversed(range(16)):
        found_i = -1
        for i in range(256):
            inter_tmp = list(inter_tmp)
            inter_tmp[2*j:2*j+2] = format(i,'02x')

            inter_tmp = ''.join(inter_tmp)

            if get_status('http://192.17.103.142:8080/mp3/hadrian2/?'+inter_tmp+ciphertext):

                if j == 15:
                    found_i_tmp = found_i
                    found_i = i
                else:
                    found_i = i
                    break

        PreXorMessage.insert(0,16^found_i)
        InterVal = found_i
        Px = PreXorMessage[0] ^ InterVal
        if j == 15:
            if int(intermediate[30:32],16)^PreXorMessage[0] == 16 and found_i_tmp:
                PreXorMessage[0] = 16^found_i_tmp
        if j != 0:

            inter_tmp = list(inter_tmp)
            for i in range(len(PreXorMessage)):
                inter_tmp[30-2*i:32-2*i] =  format(PreXorMessage[-(i+1)] ^ 16-len(PreXorMessage)+i,'02x')
    Plaintext = ''
    for i in range(16):
        if int(intermediate[2*i:2*i+2],16) ^ PreXorMessage[i] > 126 or int(intermediate[2*i:2*i+2],16) ^ PreXorMessage[i] < 32:
            pass
        else:
            Plaintext += chr(int(intermediate[2*i:2*i+2],16) ^ PreXorMessage[i])
    return Plaintext





def get_status(u):
    try:
        resp = urllib.request.urlopen(u)
        return 0
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return 1
        else:
            return 0

def pad(msg):
    n = len(msg) % 16
    return msg + ''.join(format(i,'02x') for i in range(16, n, -1))


if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    main(a,b)
