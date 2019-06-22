import time
import struct

class Ticker:
    def __init__(self):
        self.t = time.time()
    
    def __call__(self):
        dt = time.time() - self.t
        # self.t = time.time()
        return 1000 * dt

def genmask(bitMask, totalBitSize):
    return ((1 << bitMask) - 1) << (totalBitSize - bitMask)

def printBinary(data, spacer='', breakOn=4):
    hstr = ""
    pos = 0
    for x in data:
        pos += 1
        hstr = format(x, '08b') + spacer + hstr
        if breakOn != 0 and pos % breakOn == 0 and pos < len(data):
            hstr+="\n"
    
    print(hstr)
    