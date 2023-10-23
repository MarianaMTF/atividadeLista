nomes=["mariana", "renato", "enzo", "peter"]
nova_lista=[]
alfabeto=["abcdefghijklmnopqrstwxyz"]
for letra in alfabeto:
  for nome in nomes:
    if nome[0]==letra:
      nova_lista.append(nome)
print(nova_lista)
