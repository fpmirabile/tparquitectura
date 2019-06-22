import matplotlib.pyplot as plt

def configurePlot():
  # plt.axis([0, MAX_BIT_RANGE, 0, 150])
  plt.grid(True)
  plt.title('Bit Collision')
  plt.xlabel('Bits')
  plt.ylabel('Time (miliseconds)')

def executePlot(x, y):
  configurePlot()
  plt.plot(x, y)
  plt.show(block=False)

def updatePlot(x, y):
  plt.plot(x, y)
  plt.pause(0.5)
  plt.draw()

def showPlot():
  plt.show()