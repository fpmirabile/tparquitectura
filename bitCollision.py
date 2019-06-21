import matplotlib.pyplot as plt
import random
import time
import struct
import hashlib
import sys
import numpy

x = []
y = []

class Ticker:
    def __init__(self):
        self.t = time.time()
    
    def __call__(self):
        dt = time.time() - self.t
        self.t = time.time()
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
  # plt.axis([0, 256, 0, 150])
  plt.grid(True)
  plt.title('Bit Collision')
  plt.xlabel('Bits')
  plt.ylabel('Time (miliseconds)')

def executePlot():
  configurePlot()
  plt.plot(x, y)

  # for i in range(256):
    # y.append(random.randrange(0,150))
    # x.append(i)
    # plt.plot(x, y)
    # plt.pause(0.5)

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

  print(m)
  nb = struct.pack('I', m)
  printBinary(nb, " ")
  return m

genmask(1)
# bitNumber = 0
# # mask = int('10000000', 2)

# executePlot()
# nb = struct.pack('q', random.randrange(0, sys.maxsize))
# h = hashlib.sha256()
# h.update(nb)
# for biggerValue in range(150):
#     mask = genmask(int(biggerValue / 32))
#     tick = Ticker()
#     bitNumber += 1
#     digest = h.digest()
#     byteToTest = digest[0]
#     # print((first & mask) == 0)
#     if ((byteToTest & mask) == 0):
#       x.append(bitNumber)
#       y.append(tick())
#       mask = genmask(0)
#       updatePlot()

#     # print("Done in {}ms".format(tick()))
#     mask = mask << 1

# plt.show()