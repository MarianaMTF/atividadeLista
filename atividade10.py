numeros=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i=0
while i<len(numeros)-1:
  if numeros[i]%2==0:
    numeros[i]=0
  i+=1
for num in numeros:
  print(num)
