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
  return (x ** (1 / m))

xpoints = []
ypoints = []
NormYPoints = NormalRoot()

def HyunseungRootFormula():
  sum = 0

  for i in tqdm(range(repeat)):
    power = pow(np.log(x) / m ,i)

    sum += Decimal(power) / Decimal(math.factorial(i))

    xpoints.append(i)
    ypoints.append(sum)

  return sum

def graph():
  plt.plot(np.array(xpoints), np.array(ypoints), color="r", label="Hyunseung Root Formula")
  plt.axhline(y=NormalRoot(), color='b', linestyle='dotted')
  plt.show()

def main():
  norm = NormalRoot()
  hyun = HyunseungRootFormula()

  print("Normal Root: ", norm)
  print("Hyunseung Root: ", hyun)
  print("Error: " + str(abs(Decimal(norm) - hyun)))

  graph()

main()
