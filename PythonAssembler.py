# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LRRFb4ifTqRWoksZzqZIZ0qrlw4_Ow3b 
    For Magister....
"""

import numpy as np # Librerias  

ACC = 0 #Accumulative
REG = 0 #Register

memory_loc = {}
memory_reg = {}

# Rules.
codes = ["RAC","RRE","ADD", "SUB","JMP", "WAC", "FLP", "IFF", "HLT"]

# Initial condition to fibonacci.
initials = [1, 1, 0]
instructions = ["RAC", "RRE", "ADD", "WAC", "JMP", "HLT"] #Algoritmo del Fibbonaci

w,j = 0,0
while True: #We will create the memory space. j

  c, i = 0, 0
  while True: # Writtings the instructions in memory. i 
    if i == len(instructions) - 1:
      instructions.append("NULL")

    try:
      if type(initials[i]) == int:
        memory_reg["000F" + str(i)] = initials[i]

    except IndexError :
        memory_reg["000F" + str(i)] = 0

    if instructions[i] == codes[0]: #RAC
      memory_loc["000" + str(i + j + c + w)] = codes[0]
      c = c + 1
      memory_loc["000" + str(i + j + c + w)] = "000F" + str(i + j) 
      ACC = memory_reg["000F" + str(i + j)]

    if instructions[i] == codes[1]: #RRE
      memory_loc["000" + str(i + j + c + w)] = codes[1]
      c = c + 1
      memory_loc["000" + str(i + j + c + w)] = "000F" + str(i + j) 
      REG = memory_reg["000F" + str(i + j)]

    if instructions[i] == codes[2]: #ADD
      memory_loc["000" + str(i + j + c + w)] = codes[2]
      ACC = ACC + REG #entra la accion 

    if instructions[i] == codes[3]: #SUB
      memory_loc["000" + str(i + j + c + w)] = codes[3]
      ACC = abs(ACC - REG) #entra la accion 

    if instructions[i] == codes[4]: #JMP
      memory_loc["000" + str(i + j + c + w)] = codes[4] 
      c = c + 1
      memory_loc["000" + str(i + j + c + w)] = "000" + str(w + j) 
      w += len(instructions) + 2
      break

    if instructions[i] == codes[5]: #WAC
      memory_loc["000" + str(i + j + c + w)] = codes[5]
      c = c + 1
      for k in range(len(initials)):
        if initials[k] == 0:
          memory_reg["000F" + str(k)] = ACC
          initials.append(0); initials[-2]= ACC
          memory_loc["000" + str(i + j + c + w)] = "000F" + str(k)
          break
      #entra la accion y el condicional  --> 
    
    if instructions[i] == codes[6]: #FLP
      memory_loc["000" + str(i + j + c + w)] = codes[6]
      #entra la accion y el condicional

    if instructions[i] == codes[7]: #IFF
      memory_loc["000" + str(i + j + c + w)] = codes[7]
      #entra la accion y el condicional

    if i == len(instructions) - 1:
      instructions.append("NULL")

    i += 1


  if ACC >= 123:
        memory_loc["000" + str(len(memory_loc))] = codes[8] #HLT
        break

  j += 1

import pandas as pd
pd.set_option('display.max_rows', None)

df = pd.DataFrame(data=memory_loc, index=[0])
df = (df.T)
print(df)

print("\n")

ds = pd.DataFrame(data=memory_reg, index=[0])
ds = (ds.T)
print(ds)

