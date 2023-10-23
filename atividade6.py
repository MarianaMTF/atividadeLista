numeros=[1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 10]
i=0
j=1
while j<len(numeros)-1:
  if numeros[i]==numeros[j]:
    numeros.remove(numeros[j])
  i+=1
  j+=1
print(numeros)
