from pyplot.plotHelper import configurePlot, updatePlot, executePlot, showPlot
from utils.helpers import Ticker, genmask
import random
import struct
import hashlib
import sys

x = []
y = []
MAX_BIT_RANGE = 256

def hashANumber():
  nb = struct.pack('q', random.randrange(0, sys.maxsize))
  h = hashlib.sha256()
  h.update(nb)
  digest = h.digest()
  return digest  

def testBitCollision(digest, mask):
  # Length digest * 8 = 256 bits = MAX_BIT_SIZE
  print("Generated mask: {}".format(format(mask, "010b")))
  digestBits = int.from_bytes(digest, 'big')
  print("Generated digest: {}".format(format(digestBits, "08b")))
  result = digestBits & mask == 0
  return result

def execCollision():
  bitNumber = 1
  retryTime = 0
  tick = Ticker() 
  mask = genmask(bitNumber, MAX_BIT_RANGE)
  while (bitNumber < MAX_BIT_RANGE):
    print("Creating a new Hash...")
    digest = hashANumber()
    result = testBitCollision(digest, mask)
    if (result): # Si hay colision => Sumamos 1 y ejecutamos el grafico
      print("BitNumber: {} Found, going to: {}".format(bitNumber, bitNumber + 1))
      x.append(bitNumber)
      y.append(tick())
      updatePlot(x, y)
      bitNumber += 1
      mask = genmask(bitNumber, MAX_BIT_RANGE)
      retryTime = 0
    else:
      print("BitNumber: {} Not found, looking again. Try number: {}".format(bitNumber, retryTime))
      retryTime += 1

executePlot(x, y)
execCollision()
# Fix para que no cierre la ventana
showPlot()