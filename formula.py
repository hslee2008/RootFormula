# Formula m√x

import matplotlib.pyplot as plt
import numpy as np
import math
from tqdm import tqdm
from decimal import *

getcontext().prec = 999
m = int(input("Enter m: "))
x = int(input("Enter x: "))
repeat = int(input("Enter repeat: "))

def NormalRoot():
  return (Decimal(x) ** (Decimal(1) / Decimal(m)))

xpoints = []
ypoints = []
difXPoints = []
difYPoints = []

NormYPoints = NormalRoot()

def HyunseungRootFormula():
  sum = 0

  for i in tqdm(range(repeat)):
    power = pow(Decimal(x).ln() / m ,i)

    sum += Decimal(power) / Decimal(math.factorial(i))

    xpoints.append(i)
    ypoints.append(sum)

    if (i > repeat - 10):
      difXPoints.append(i)
      difYPoints.append(abs(Decimal(NormYPoints) - sum))

  return sum

def graph():
  plt.subplot(1, 2, 1)
  plt.plot(np.array(xpoints), np.array(ypoints), color="r", label="Hyunseung Root Formula")
  plt.axhline(y=NormalRoot(), color='b', linestyle='dotted')

  plt.subplot(1, 2, 2)
  plt.plot(np.array(difXPoints), np.array(difYPoints), color="r", label="Hyunseung Root Formula Difference")

  plt.show()

def main():
  norm = NormalRoot()
  hyun = HyunseungRootFormula()

  print("Normal Root: ", norm)
  print("Hyunseung Root: ", hyun)
  print("Error: " + str(abs(Decimal(norm) - hyun)))

  graph()

main()
