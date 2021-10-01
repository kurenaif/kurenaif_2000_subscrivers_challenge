from Crypto.Util.number import *

flag = bytes_to_long(b"kurenaifCTF{DUMMYDUMMYDUMMYDUMMYDUMMYDUMMYDUMMY}")
print("# bit_length = ", flag.bit_length())
e = 20000

ns = []
cs = []

for i in range(2*200):
    p = getPrime(20)
    q = getPrime(20)
    n = p * q
    ns.append(n)
    cs.append(pow(flag, e, n))

print("e=", e)
print("ns=", ns)
print("cs=", cs)
