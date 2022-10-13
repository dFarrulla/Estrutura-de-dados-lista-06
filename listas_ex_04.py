'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.'''
cons = []
vogais = ["a", "e", "i", "o", "u"]
contavogal = 0
for i in range(1, 11):
  letras = (input("Digite uma letra: "))
  if letras in vogais:
    pass
  else:
    contavogal += 1
    cons.append(letras)
print(cons)