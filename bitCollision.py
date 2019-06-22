import matplotlib.pyplot as plt
import random
import time
import struct
import hashlib
import sys
import numpy

x = []
y = []
MAX_BIT_RANGE = 256

class Ticker:
    def __init__(self):
        self.t = time.time()
    
    def __call__(self):
        dt = time.time() - self.t
        # self.t = time.time()
        return 1000 * dt

def printBinary(data, spacer='', breakOn=4):
    hstr = ""
    pos = 0
    for x in data:
        pos += 1
        hstr = format(x, '08b') + spacer + hstr
        if breakOn != 0 and pos % breakOn == 0 and pos < len(data):
            hstr+="\n"
    
    print(hstr)

def configurePlot():
  # plt.axis([0, MAX_BIT_RANGE, 0, 150])
  plt.grid(True)
  plt.title('Bit Collision')
  plt.xlabel('Bits')
  plt.ylabel('Time (miliseconds)')

def executePlot():
  configurePlot()
  plt.plot(x, y)
  plt.show(block=False)

def updatePlot():
  plt.plot(x, y)
  plt.pause(0.5)
  plt.draw()

def genmask(n):
  n = 32 - n
  m = numpy.uint32(0)
  for i in range(32, n, -1):
    m = m + 2**(i-1)

  # print(m)
  # nb = struct.pack('I', m)
  # printBinary(nb, " ")
  return m

def hashANumber():
  nb = struct.pack('q', random.randrange(0, sys.maxsize))
  h = hashlib.sha256()
  h.update(nb)
  digest = h.digest()
  return digest  

def matchABit(digest, bitNumber, tick):
  mask = genmask(bitNumber)

  for digestIndex in range(len(digest)):
    byteToTest = digest[digestIndex]
    if ((byteToTest & mask) == 0):
      x.append(bitNumber)
      y.append(tick())
      updatePlot()
      break

def execCollision():
  tick = Ticker()
  for bitNumber in range(1, MAX_BIT_RANGE + 1):
    digest = hashANumber()
    matchABit(digest, bitNumber, tick)

executePlot()
execCollision()
plt.show()