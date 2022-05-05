import sys
import math
import numpy as np
from Crypto.Util.number import isPrime
from Crypto.Util.number import inverse
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_v1_5
import pbp

class PRTree:
    def __init__(self,val,prod1=None,prod2=None):
        self.prod1 = prod1
        self.prod2 = prod2
        self.mod = None
        self.val = val

    def __mul__(self,other):
        return PRTree((self.val*other.val),self,other)

    def modulus_root(self):
        self.prod1.mod = self.val%(self.prod1.val**2)
        self.prod2.mod = self.val%(self.prod2.val**2)

    def modulus(self):
        if self.prod1:
            print('Calculating parent1 Mod')
            self.prod1.mod = self.mod%(self.prod1.val**2)
        if self.prod2:
            print('Calculating parent2 Mod')
            self.prod2.mod = self.mod%(self.prod2.val**2)
        print('Done')

def gcd(a,b):
    if (b == 0):
        return a
    else:
        return gcd(b,a%b)



def main(in_moduli,in_E,in_cipher,out_plain):

    Level = []
    num_mod = 10000
    for i in range(15):
        Level.append([])
    with open(in_moduli) as f:
        for line in f:
            Level[0].append(PRTree(int(line.strip(),16)))
    with open(in_cipher) as g:
        inHex = "".join(g.readlines())
        print(inHex)
    for i in range(14):
        maxj = int(math.ceil(len(Level[i])/2))
        print(len(Level[i])/2 % 1)
        if len(Level[i])/2 % 1 != 0:
            for j in range(maxj):
                if j == maxj-1:
                    Level[i+1].append(Level[i][2*j])
                else:
                    Level[i+1].append(Level[i][2*j]*Level[i][2*j+1])
        else:
            for j in range(maxj):
                Level[i+1].append(Level[i][2*j]*Level[i][2*j+1])
    print(len(Level[14]))
    Level[14][0].modulus_root()
    for i in reversed(range(1,14)):
        print(i)
        print(len(Level[i]))
        for j in range(len(Level[i])):

            Level[i][j].modulus()

    Ps = []
    MPQs = []
    for i in range(num_mod):
        Ps.append(gcd(int(Level[0][i].mod)//int(Level[0][i].val),int(Level[0][i].val)))

    for i in range(len(Ps)):
        if Ps[i] != 1:
            MPQs.append([Level[0][i].val,Ps[i],Level[0][i].val//Ps[i]])



    keys = []
    for i in range(len(MPQs)):
        print(i)
        try:
            D = inverse(65537,((MPQs[i][1]-1)*(MPQs[i][2]-1)))
            print(D)
        except:
            print("no mod inv")
            continue
        try:
            print(MPQs[i][0])
            key = RSA.construct((int(MPQs[i][0]),65537,int(D),MPQs[i][1],MPQs[i][2]))
            print(key)
        except:
            print('no key')
            continue
        try:
            plaintext = pbp.decrypt(key,inHex)
            print(plaintext)
            break
        except:
            print('no decrypt')






if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    d = sys.argv[4]
    main(a,b,c,d)
