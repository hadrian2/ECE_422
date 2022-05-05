import sys
from Crypto.Cipher import AES
def main(text, key, iv, out):
    with open(text) as f:
        textHex = f.read().strip()
    with open(key) as k:
        keyHex = k.read().strip()
    with open(iv) as i:
        ivHex = i.read().strip()


    if len(bytes.fromhex(textHex)) % 16 == 0 and len(bytes.fromhex(keyHex)) % 16 == 0 and len(bytes.fromhex(ivHex)) % 16 == 0:
        textBytes = bytes.fromhex(textHex)
        keyBytes = bytes.fromhex(keyHex)
        ivBytes = bytes.fromhex(ivHex)
    else:
        print("Incorrect length for cipher text, key, or IV")
        return

    cipher = AES.new(keyBytes, AES.MODE_CBC, ivBytes)

    plaintext = cipher.decrypt(textBytes).decode('utf-8')

    with open(out, 'w') as o:
        o.write(plaintext)



if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    d = sys.argv[4]
    main(a,b,c,d)
