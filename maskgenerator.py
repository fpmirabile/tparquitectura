import hashlib
import struct
import random
import sys

def hashANumber():
  nb = struct.pack('q', random.randrange(0, sys.maxsize))
  h = hashlib.sha256()
  h.update(nb)
  digest = h.digest()
  return digest  

def masking(n, m):
    return ((1 << n) - 1) << (m - n)

def printBinary(data, spacer='', breakOn=4):
    hstr = ""
    pos = 0
    for x in data:
        pos += 1
        hstr = format(x, '08b') + spacer + hstr
        if breakOn != 0 and pos % breakOn == 0 and pos < len(data):
            hstr+="\n"
    
    print(hstr)

def test_0bits(digest_bytes, n_bits):
    m = 8 * len(digest_bytes)
    digest_num = int.from_bytes(digest_bytes, 'big')
    print(digest_num)
    mask = masking(n_bits, m)
    print(format(mask, "08b"))
    # nb = struct.pack('q', mask)
    # printBinary(nb, ' ')
    return digest_num & mask == 0

print(test_0bits(hashANumber(), 0))
print(test_0bits(hashANumber(), 1))
print(test_0bits(hashANumber(), 2))
print(test_0bits(hashANumber(), 3))
print(test_0bits(hashANumber(), 4))
print(test_0bits(hashANumber(), 5))
print(test_0bits(hashANumber(), 6))

