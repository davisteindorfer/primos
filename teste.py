primos = []
for c in range (10,1000):
  for i in range (2,c):
    if c % i == 0:
      break
  else:
      primos.append(c)
      

      
print(primos)
