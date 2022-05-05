import sys
def main(text, key, mod, out):
    with open(text) as f:
        textHex = f.read().strip()
    with open(key) as k:
        keyHex = k.read().strip()
    with open(mod) as i:
        modHex = i.read().strip()

    textInt = int(textHex, 16)
    keyInt = int(keyHex, 16)
    modInt = int(modHex, 16)

    plaintext = pow(textInt,keyInt,modInt)

    with open(out,'w') as o:
        o.write(hex(plaintext)[2:])




if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    d = sys.argv[4]
    main(a,b,c,d)
