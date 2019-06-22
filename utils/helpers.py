import time

class Ticker:
    def __init__(self):
        self.t = time.time()
    
    def __call__(self):
        dt = time.time() - self.t
        # self.t = time.time()
        return 1000 * dt

def genmask(bitMask, totalBitSize):
    return ((1 << bitMask) - 1) << (totalBitSize - bitMask)