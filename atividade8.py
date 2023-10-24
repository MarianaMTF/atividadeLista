menor=0
maior=0
numeros=[1, 2, 3, 4, 5]
for num in numeros:
  if menor>num:
    menor=num
for num in numeros:
  if maior<num:
    maior=num
print(f"{maior} é maior")
print(f"{menor} é menor")
