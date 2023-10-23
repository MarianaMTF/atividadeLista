compras=[]
while True:
  compra=input("digite a sua compra(digite "0" para sair):")
  if compra==0:
    break
  compras.append(compra)
for compra in compras:
  print(compra)
