'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.'''
num = [[],[]]
valor = 0
for c in range (1, 8):
  valor = int(input(f'Digite o {c}o: '))
  if valor % 2 == 0:
    num[0].append(valor)
  else:
    num[1].append(valor)
print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores pares digitados foram: {num[1]}')
  