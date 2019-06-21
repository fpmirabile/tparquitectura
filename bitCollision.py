import matplotlib.pyplot as plt
import random
import time
import struct
import hashlib
import sys

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

bitNumber = 0
mask = int('11111111', 2)
tick = Ticker()

executePlot()
nb = struct.pack('i', 26081992)
h = hashlib.sha256()
h.update(nb)
for biggerValue in range(100):
    tick()
    bitNumber += 1
    digest = h.digest()
    byteToTest = digest[0]
    # print((first & mask) == 0)
    if ((byteToTest & mask) == 0):
      x.append(bitNumber)
      y.append(tick())
      mask = int('11111111', 2)
      updatePlot()

    # print("Done in {}ms".format(tick()))
    mask = mask << 1

plt.show()