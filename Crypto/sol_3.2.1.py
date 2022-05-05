import sys
from pymd5 import md5, padding
from urllib.parse import quote_from_bytes
def main(in_query, in_command, out_query):

    with open(in_query) as f:
        original_query = f.read().strip()
    with open(in_command) as i:
        malicious_command = i.read().strip()


    concat_to_pass = original_query[original_query.index('user='):]
    length_of_m = (8+len(concat_to_pass))
    bit_count = (length_of_m+len(padding(length_of_m*8)))*8

    original_hash = original_query[6:original_query.index('&user=')]
    hash_slinging_slasher = md5(state = original_hash, count = bit_count)
    hash_slinging_slasher.update(malicious_command.encode())

    modified_query = original_query[:6]+hash_slinging_slasher.hexdigest()+original_query[original_query.index('&user='):]+quote_from_bytes(padding(length_of_m*8))+malicious_command

    with open(out_query, 'w') as o:
        o.write(modified_query)

if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    main(a,b,c)
