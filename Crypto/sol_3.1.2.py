import sys
def main(text,key,out):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out_string = ""
    with open(text) as f:
        cipher_string = f.read().strip()
    with open(key) as k:
        cipher_key = k.read().strip()
    for i in range(len(cipher_string)):
        if cipher_string[i] in cipher_key:
            out_string = out_string + alphabet[cipher_key.index(cipher_string[i])]
        else:
            out_string = out_string + cipher_string[i]
    with open(out, 'w') as o:
        o.write(out_string)

if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    main(a,b,c)
