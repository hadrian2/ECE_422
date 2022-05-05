import sys
def main(in_plain, out_hex):
    mask = 0x3FFFFFFF
    out_hash = 0

    with open(in_plain) as f:
        inStr = f.read().strip()

    inHex = ""
    for i in range(len(inStr)):
        inHex += hex(ord(inStr[i]))[2:]

    inBytes = bytes.fromhex(inHex)

    for byte in inBytes:
        intermediate_val = ((byte ^ 0xCC) << 24 ) | ((byte ^ 0x33) << 16) | ((byte ^ 0xAA) << 8) | (byte ^ 0x55)
        out_hash = (out_hash & mask) + (intermediate_val & mask)

    outHex = hex(out_hash)[2:]
    with open(out_hex, 'w') as o:
        o.write(outHex)


if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    main(a,b)
